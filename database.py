from pymongo import MongoClient

# connect to mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client['pitch_management']
collection = db['pitches']
