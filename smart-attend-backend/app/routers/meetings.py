from fastapi import APIRouter
from ..models import Meeting
from ..crud import get_meetings

router = APIRouter(prefix="/meetings", tags=["meetings"])

@router.get("/{course_id}")
def list_meetings(course_id: str):
    return get_meetings(course_id)
