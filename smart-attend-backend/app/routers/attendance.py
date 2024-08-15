from fastapi import APIRouter, File, UploadFile
from ..models import Attendance
from ..crud import create_attendance_record, get_attendance_records
from ..utils import process_attendance_from_video

router = APIRouter(prefix="/attendance", tags=["attendance"])

@router.post("/")
def add_attendance(record: Attendance):
    create_attendance_record(record)
    return {"status": "Attendance recorded"}

@router.get("/{course_id}")
def list_attendance(course_id: str):
    return get_attendance_records(course_id)

@router.post("/process-video")
async def process_attendance_video(file: UploadFile = File(...)):
    # Save the uploaded video file
    video_path = f"temp_videos/{file.filename}"
    with open(video_path, "wb") as f:
        f.write(file.file.read())
    
    # Process the video to extract attendance
    process_attendance_from_video(video_path)
    
    return {"status": "Attendance processed from video"}
