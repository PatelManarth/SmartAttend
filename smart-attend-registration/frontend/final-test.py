from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import time
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient

from win32com.client import Dispatch

def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

def send_email(to_email, subject, body):
    USER = "smartattend@outlook.com"
    PASSWORD = "password"

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
        server.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Initialize MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client["attendance_db"]
collection = db["attendance_records"]

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

with open('data/names.pkl', 'rb') as w:
    LABELS = pickle.load(w)
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

print('Shape of Faces matrix --> ', FACES.shape)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

imgBackground = cv2.imread("background.png")

attendance_count = {}  # Dictionary to track frame count for each detected face
start_time = time.time()

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)[0]
        
        ts = time.time()
        timestamp = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

        # Track attendance count
        if output in attendance_count:
            attendance_count[output] += 1
        else:
            attendance_count[output] = 1

        # Check if face detected in 10 frames within 5 seconds
        if attendance_count[output] >= 10 and (ts - start_time) <= 5:
            attendance = {
                "name": str(output),
                "timestamp": timestamp
            }

            # Insert attendance record into MongoDB
            collection.insert_one(attendance)
            speak("Attendance Taken.")

            # Send email
            subject = "Attendance Confirmation"
            body = f"Dear Student,\n\nYour attendance has been marked at {timestamp}.\n\nBest regards,\nAttendance System"
            send_email("student@example.com", subject, body)  # Replace with actual student email
            time.sleep(5)

    imgBackground[162:162 + 480, 55:55 + 640] = frame
    cv2.imshow("Frame", imgBackground)
    k = cv2.waitKey(1)

    if k == ord('q'):
        break

    # Reset the start time and attendance count if time exceeds 5 seconds
    if time.time() - start_time > 5:
        start_time = time.time()
        attendance_count.clear()

video.release()
cv2.destroyAllWindows()
