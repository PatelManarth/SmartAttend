from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['attendance']

# Create collections if they don't exist
if 'students' not in db.list_collection_names():
    db.create_collection('students')

if 'scheduled_classes' not in db.list_collection_names():
    db.create_collection('scheduled_classes')
