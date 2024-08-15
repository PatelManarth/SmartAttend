from fastapi import APIRouter
from ..models import Meeting
from ..crud import create_meeting, get_meetings

router = APIRouter(prefix="/meetings", tags=["meetings"])

@router.post("/")
def schedule_meeting(meeting: Meeting):
    create_meeting(meeting)
    return {"status": "Meeting scheduled"}

@router.get("/{course_id}")
def list_meetings(course_id: str):
    return get_meetings(course_id)
