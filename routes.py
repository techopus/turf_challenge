from flask import jsonify, request
from models import Pitch
from database import collection
from bson import ObjectId

def index():
    return 'Flask application is running!'


# @app.route('/pitches', methods=['GET'])
# def get_pitches():
#     pitches = list(collection.find())
#     return jsonify({'pitches': pitches})

def get_pitches():
    pitches = list(collection.find())
    # Convert each pitch document to a dictionary with a string ID
    pitches_serializable = [{
        **pitch,
        '_id': str(pitch['_id'])  # Convert ObjectId to string
    } for pitch in pitches]
    return jsonify({'pitches': pitches_serializable})

def create_pitch():
    data = request.json
    pitch = Pitch(**data)
    result = collection.insert_one(pitch.__dict__)
    return jsonify({'id': str(result.inserted_id)})

# @app.route('/pitches/<id>', methods=['GET'])
# def get_pitch(id):
#     pitch = collection.find_one({'_id': ObjectId(id)})
#     return jsonify({'pitch': pitch})

def get_pitch(id):
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

def update_pitch(id):
    data = request.json
    collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'Pitch updated successfully'})

def delete_pitch(id):
    collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Pitch deleted successfully'})

# @app.route('/pitches/maintenance', methods=['GET'])
# def get_pitches_needing_maintenance():
#     pitches = list(collection.find({'health_score': {'$lt': 10}}))
#     return jsonify({'pitches': pitches})

def get_pitches_needing_maintenance():
    pitches = list(collection.find({'health_score': {'$lt': 10}}))
    # Convert each pitch document to a dictionary with a string ID
    pitches_serializable = [{
        **pitch,
        '_id': str(pitch['_id'])  # Convert ObjectId to string
    } for pitch in pitches]
    return jsonify({'pitches': pitches_serializable})

# @app.route('/pitches/replacement', methods=['GET'])
# def get_pitches_needing_replacement():
#     pitches = list(collection.find({'health_score': 2}))
#     return jsonify({'pitches': pitches})

def get_pitches_needing_replacement():
    pitches = list(collection.find({'health_score': 2}))
    # Convert each pitch document to a dictionary with a string ID
    pitches_serializable = [{
        **pitch,
        '_id': str(pitch['_id'])  # Convert ObjectId to string
    } for pitch in pitches]
    return jsonify({'pitches': pitches_serializable})
