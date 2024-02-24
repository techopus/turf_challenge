from flask import Flask
from routes import index, get_pitches, create_pitch, get_pitch, update_pitch, delete_pitch, get_pitches_needing_maintenance, get_pitches_needing_replacement

app = Flask(__name__)

# Register routes
app.add_url_rule('/', view_func=index)
app.add_url_rule('/pitches', view_func=get_pitches, methods=['GET'])
app.add_url_rule('/pitches', view_func=create_pitch, methods=['POST'])
app.add_url_rule('/pitches/<id>', view_func=get_pitch, methods=['GET'])
app.add_url_rule('/pitches/<id>', view_func=update_pitch, methods=['PUT'])
app.add_url_rule('/pitches/<id>', view_func=delete_pitch, methods=['DELETE'])
app.add_url_rule('/pitches/maintenance', view_func=get_pitches_needing_maintenance, methods=['GET'])
app.add_url_rule('/pitches/replacement', view_func=get_pitches_needing_replacement, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)