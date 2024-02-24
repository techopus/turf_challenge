from flask import jsonify, request
from models import Pitch
from database import collection
from bson import ObjectId
from utils import simulate_drying, calculate_health_score, schedule_maintenance, schedule_replacement


def index():
    return 'Flask application is running!'


def get_pitches():
    try:
        pitches = list(collection.find())
        # Convert each pitch document to a dictionary with a string ID
        pitches_serializable = [{
            **pitch,
            '_id': str(pitch['_id'])  # Convert ObjectId to string
        } for pitch in pitches]
        return jsonify({'pitches': pitches_serializable})
    except Exception as e:
        return jsonify({'message': f'Error fetching pitches: {e}'}), 500

def create_pitch():
    try:
        data = request.json
        pitch = Pitch(**data)
        result = collection.insert_one(pitch.__dict__)
        return jsonify({'id': str(result.inserted_id)})
    except Exception as e:
        return jsonify({'message': f'Error creating pitch: {e}'}), 500

def get_pitch(id):
    try:
        pitch = collection.find_one({'_id': ObjectId(id)})
        if pitch:
            # Convert the pitch document to a dictionary with a string ID
            pitch_serializable = {
                **pitch,
                '_id': str(pitch['_id'])  # Convert ObjectId to string
            }
            return jsonify({'pitch': pitch_serializable})
        else:
            return jsonify({'message': 'Pitch not found'}), 404
    except Exception as e:
        return jsonify({'message': f'Error fetching pitch: {e}'}), 500

def update_pitch(id):
    try:
        data = request.json
        collection.update_one({'_id': ObjectId(id)}, {'$set': data})
        return jsonify({'message': 'Pitch updated successfully'})
    except Exception as e:
        return jsonify({'message': f'Error updating pitch: {e}'}), 500

def delete_pitch(id):
    try:
        collection.delete_one({'_id': ObjectId(id)})
        return jsonify({'message': 'Pitch deleted successfully'})
    except Exception as e:
        return jsonify({'message': f'Error deleting pitch: {e}'}), 500



#  Monitoring endpoints

def get_pitches_needing_maintenance():
    try:
        pitches = list(collection.find())
        pitches_needing_maintenance = []

        for pitch in pitches:
            last_maintenance_date = pitch['last_maintenance_date']
            health_score = pitch['current_condition']
            turf_type = pitch['turf_type']
            rain_duration = 0  # Assume no rain for now but parameter removed from simulate func

            drying_time = simulate_drying(turf_type)
            maintenance_date, new_health_score = schedule_maintenance(last_maintenance_date, health_score, turf_type)

            if maintenance_date and new_health_score:
                pitch['next_scheduled_maintenance'] = maintenance_date
                pitch['current_condition'] = new_health_score
                collection.update_one({'_id': pitch['_id']}, {'$set': pitch})
                pitches_needing_maintenance.append(pitch)

        pitches_serializable = [{
            **pitch,
            '_id': str(pitch['_id'])  # Convert ObjectId to string
        } for pitch in pitches_needing_maintenance]

        return jsonify({'pitches': pitches_serializable})
    except Exception as e:
        return jsonify({'message': f'Error fetching pitches needing maintenance: {e}'}), 500

def get_pitches_needing_replacement():
    try:
        pitches = list(collection.find())
        pitches_needing_replacement = []

        for pitch in pitches:
            health_score = pitch['current_condition']
            turf_type = pitch['turf_type']

            if health_score == 2:
                replacement_date = schedule_replacement(health_score)
                pitch['replacement_date'] = replacement_date
                pitches_needing_replacement.append(pitch)

        pitches_serializable = [{
            **pitch,
            '_id': str(pitch['_id'])  # Convert ObjectId to string
        } for pitch in pitches_needing_replacement]

        return jsonify({'pitches': pitches_serializable})
    except Exception as e:
        return jsonify({'message': f'Error fetching pitches needing replacement: {e}'}), 500