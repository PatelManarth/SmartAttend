from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['attendance_system']

def get_attendance_collection(course_id):
    collection_name = f'attendance_{course_id}'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    return db[collection_name]

def get_meeting_collection():
    if 'meetings' not in db.list_collection_names():
        db.create_collection('meetings')
    return db['meetings']
