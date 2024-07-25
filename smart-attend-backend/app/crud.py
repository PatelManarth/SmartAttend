from .models import Student, AttendanceRecord, ScheduledClass
from .database import get_student_collection, get_attendance_collection, get_scheduled_classes_collection
from .utils import generate_student_id

student_collection = get_student_collection()
scheduled_classes_collection = get_scheduled_classes_collection()

def create_student(student: Student):
    student.student_id = generate_student_id()
    student_collection.insert_one(student.model_dump())

def get_students():
    return list(student_collection.find({}, {'_id': 0}))

def create_attendance_record(record: AttendanceRecord):
    attendance_collection = get_attendance_collection(record.course)
    attendance_collection.insert_one(record.model_dump())

def get_attendance_records(course):
    attendance_collection = get_attendance_collection(course)
    return list(attendance_collection.find({}, {'_id': 0}))

def create_scheduled_class(scheduled_class: ScheduledClass):
    scheduled_classes_collection.insert_one(scheduled_class.model_dump())

def get_scheduled_classes():
    return list(scheduled_classes_collection.find({}, {'_id': 0}))
