from fastapi import APIRouter
from typing import List
from ..models import AttendanceRecord, ScheduledClass
from ..crud import create_attendance_record, get_attendance_records, create_scheduled_class, get_scheduled_classes

router = APIRouter(
    prefix="/attendance",
    tags=["attendance"]
)

@router.post("/", response_model=AttendanceRecord)
def add_attendance(record: AttendanceRecord):
    create_attendance_record(record)
    return record

@router.get("/{course}", response_model=List[AttendanceRecord])
def list_attendance(course: str):
    return get_attendance_records(course)

@router.post("/schedule", response_model=ScheduledClass)
def add_scheduled_class(scheduled_class: ScheduledClass):
    create_scheduled_class(scheduled_class)
    return scheduled_class

@router.get("/schedule", response_model=List[ScheduledClass])
def list_scheduled_classes():
    return get_scheduled_classes()
