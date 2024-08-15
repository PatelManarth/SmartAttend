from .models import Attendance, Meeting
from .database import get_attendance_collection, get_meeting_collection

def create_attendance_record(record: Attendance):
    attendance_collection = get_attendance_collection(record.course_id)
    attendance_collection.insert_one(record.dict())

def get_attendance_records(course_id):
    attendance_collection = get_attendance_collection(course_id)
    return list(attendance_collection.find({}, {'_id': 0}))

def create_meeting(meeting: Meeting):
    meeting_collection = get_meeting_collection()
    meeting_collection.insert_one(meeting.dict())

def get_meetings(course_id):
    meeting_collection = get_meeting_collection()
    return list(meeting_collection.find({"course_id": course_id}, {'_id': 0}))
