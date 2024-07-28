from fastapi import APIRouter
from typing import List
from ..models import Student
from ..crud import create_student, get_students

router = APIRouter(
    prefix="/students",
    tags=["students"]
)

@router.post("/", response_model=Student)
def register_student(student: Student):
    create_student(student)
    return student

@router.get("/", response_model=List[Student])
def list_students():
    return get_students()
