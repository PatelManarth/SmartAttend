from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    username: str
    password: str
    user_type: str  # 'student' or 'faculty'

class Meeting(BaseModel):
    meeting_id: str
    course_id: str
    faculty_id: str
    start_time: str
    end_time: str

class Attendance(BaseModel):
    student_id: str
    course_id: str
    meeting_id: str
    status: str  # 'present', 'absent', 'unknown'
    timestamp: str
