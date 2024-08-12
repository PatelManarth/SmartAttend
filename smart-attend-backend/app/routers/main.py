from fastapi import FastAPI, APIRouter
from typing import List
from ..models import Student, AttendanceRecord, ScheduledClass
from ..crud import (create_student, get_students, 
                    create_attendance_record, get_attendance_records, 
                    create_scheduled_class, get_scheduled_classes)
from ..email import send_email

app = FastAPI()

router = APIRouter()

@router.post("/students/")
async def create_student(student: Student):
    db = get_database()
    collection = db['students']
    
    # Check if the student already exists
    existing_student = collection.find_one({"email": student.email})
    if existing_student:
        return {"message": "Student already registered"}

    # Insert new student
    student_data = {
        "_id": student.student_id,
        "email": student.email,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "year_of_study": student.year_of_study,
        "courses": student.courses,
        "attendance_records": []
    }
    collection.insert_one(student_data)
    return {"message": "Student registered successfully"}


@router.post("/attendance/schedule", response_model=ScheduledClass)
def add_scheduled_class(scheduled_class: ScheduledClass):
    create_scheduled_class(scheduled_class)
    # Notify students
    students = get_students()
    course_students = [s for s in students if scheduled_class.course in s.courses]
    for student in course_students:
        send_email(
            subject="New Scheduled Class",
            recipient=student.email,
            body=f"A new class for the course {scheduled_class.course} has been scheduled on {scheduled_class.date} from {scheduled_class.start_time} to {scheduled_class.end_time}."
        )
    return scheduled_class
