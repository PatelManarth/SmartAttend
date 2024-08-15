from fastapi import APIRouter
from ..models import Attendance
from ..crud import create_attendance_record, get_attendance_records

router = APIRouter(prefix="/attendance", tags=["attendance"])

@router.post("/")
def add_attendance(record: Attendance):
    create_attendance_record(record)
    return {"status": "Attendance recorded"}

@router.get("/{course_id}")
def list_attendance(course_id: str):
    return get_attendance_records(course_id)
