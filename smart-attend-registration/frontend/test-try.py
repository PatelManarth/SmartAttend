from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import cv2
import numpy as np
import base64
from PIL import Image
from io import BytesIO
import pickle
import time
from datetime import datetime
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from win32com.client import Dispatch

# Setup Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headlessly
service = Service("C:/Users/manar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # Update path to ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the webpage
driver.get("http://localhost:3000")

# Locate the video and canvas elements
video_element = driver.find_element(By.ID, "self-view-video")
canvas_element = driver.find_element(By.ID, "participant-canvas")

# Initialize MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client["attendance_db"]
collection = db["attendance_records"]

def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

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
        server.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Capture video frame from canvas
    canvas_data = driver.execute_script("return arguments[0].toDataURL('image/png').substring(22);", canvas_element)
    image_data = base64.b64decode(canvas_data)
    image = Image.open(BytesIO(image_data))
    frame = np.array(image)

    if frame is not None:
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

            # Insert attendance record into MongoDB and send email
            attendance = {
                "name": str(output),
                "timestamp": timestamp
            }
            collection.insert_one(attendance)
            speak("Attendance Taken.")
            # Fetch student email from MongoDB and send email
            student = collection.find_one({"name": str(output)})
            if student:
                send_email(student['email'], "Attendance Confirmation", f"Dear {student['name']},\n\nYour attendance has been marked at {timestamp}.\n\nBest regards,\nAttendance System")
            time.sleep(5)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

driver.quit()
cv2.destroyAllWindows()
