import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from typing import List
from ..models import Student
from ..crud import create_student, get_students

# Add your Gmail credentials here


router = APIRouter(
    prefix="/students",
    tags=["students"]
)

# Function to send email
def send_email(to_email, subject, body):
    USER = "smartattend@outlook.com"
    PASSWORD = "autoattend@1234"

    try:
        msg = MIMEMultipart()
        msg['From'] = USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(USER, PASSWORD)
        text = msg.as_string()
        server.sendmail(to_email, to_email, text)
        #server.send_message(msg)
        server.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

@router.post("/", response_model=Student)
def register_student(student: Student):
    # Create student in the database
    create_student(student)
    
    # Connect to MongoDB to fetch faculty details
    client = MongoClient("mongodb://localhost:27017/")
    db = client["college"]
    faculty_collection = db["faculty"]

    for course in student.courses:
        # Retrieve faculty email for the course
        faculty = faculty_collection.find_one({"course": course})
        if not faculty:
            raise HTTPException(status_code=404, detail=f"Faculty not found for course: {course}")
        
        faculty_email = faculty["email"]
        faculty_name = faculty["faculty_name"]

        # Send email to the faculty
        subject = f"New Student Registration for {course}"
        body = f"Dear {faculty_name},\n\nA new student ({student.first_name} {student.last_name}) has registered for your course: {course}.\n\nBest regards,\nSmart Attend System"
        send_email(faculty_email, subject, body)

        # Send email to the student
        subject = f"Successfully Registered for {course}"
        body = f"Dear {student.first_name} {student.last_name},\n\nYou have successfully registered for the course: {course}.\n\nBest regards,\nSmart Attend System"
        send_email(student.email, subject, body)

    return student


@router.get("/", response_model=List[Student])
def list_students():
    return get_students()