from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['attendance']

def get_student_collection():
    return db['students']

def get_attendance_collection(course):
    return db[f'attendance_{course}']

def get_scheduled_classes_collection():
    return db['scheduled_classes']
