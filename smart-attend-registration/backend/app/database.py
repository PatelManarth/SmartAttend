from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['attendance']

def get_student_collection():
    if 'students' not in db.list_collection_names():
        db.create_collection('students')
    return db['students']

def get_attendance_collection(course):
    collection_name = f'attendance_{course}'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    return db[collection_name]

def get_scheduled_classes_collection():
    if 'scheduled_classes' not in db.list_collection_names():
        db.create_collection('scheduled_classes')
    return db['scheduled_classes']
