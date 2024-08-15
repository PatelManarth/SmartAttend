from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    student_id: str
    email: str
    first_name: str
    last_name: str
    year_of_study: int
    password: str  # Add password field (hashed)
    courses: List[str]

class AttendanceRecord(BaseModel):
    course: str
    student_id: str
    check_in_time: str
    check_out_time: str
    break_duration: str
    status: str  # 'present', 'late', 'left_early', 'break'

class ScheduledClass(BaseModel):
    course: str
    date: str
    start_time: str
    end_time: str
    faculty: str
