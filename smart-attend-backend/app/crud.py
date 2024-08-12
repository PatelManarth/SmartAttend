from .models import Student, AttendanceRecord, ScheduledClass
from .database import db
from .utils import generate_student_id

student_collection = db['students']
scheduled_classes_collection = db['scheduled_classes']

def create_student(student: Student):
    student.student_id = generate_student_id()
    student_collection.insert_one(student.model_dump())

def get_students():
    return list(student_collection.find({}, {'_id': 0}))

def create_attendance_record(record: AttendanceRecord):
    collection_name = f'attendance_{record.course}'
    attendance_collection = db[collection_name]
    attendance_collection.insert_one(record.model_dump())

def get_attendance_records(course):
    collection_name = f'attendance_{course}'
    attendance_collection = db[collection_name]
    return list(attendance_collection.find({}, {'_id': 0}))

def create_scheduled_class(scheduled_class: ScheduledClass):
    scheduled_classes_collection.insert_one(scheduled_class.model_dump())

def get_scheduled_classes():
    return list(scheduled_classes_collection.find({}, {'_id': 0}))
