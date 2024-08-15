import streamlit as st
import cv2
import numpy as np
import os
import pickle
import requests
from utils import generate_student_id
from hashlib import sha256

# API endpoint
API_URL = "http://localhost:8000"

# Helper function to capture images
def capture_images(name):
    video = cv2.VideoCapture(0)
    facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces_data = []
    i = 0

    stframe = st.empty()
    while len(faces_data) < 100:
        ret, frame = video.read()
        if not ret:
            st.error("Failed to capture image from camera.")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            crop_img = frame[y:y + h, x:x + w]
            resized_img = cv2.resize(crop_img, (50, 50))
            if len(faces_data) < 100 and i % 10 == 0:
                faces_data.append(resized_img)
            i += 1
            cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)
        stframe.image(frame, channels="BGR")
        if len(faces_data) >= 100:
            break

    video.release()
    faces_data = np.asarray(faces_data)
    faces_data = faces_data.reshape(100, -1)

    # Save names
    names_path = 'data/names.pkl'
    if not os.path.exists(names_path) or os.path.getsize(names_path) == 0:
        names = [name] * 100
        with open(names_path, 'wb') as f:
            pickle.dump(names, f)
    else:
        with open(names_path, 'rb') as f:
            names = pickle.load(f)
        names.extend([name] * 100)
        with open(names_path, 'wb') as f:
            pickle.dump(names, f)

    # Save faces data
    faces_data_path = 'data/faces_data.pkl'
    if not os.path.exists(faces_data_path) or os.path.getsize(faces_data_path) == 0:
        with open(faces_data_path, 'wb') as f:
            pickle.dump(faces_data, f)
    else:
        with open(faces_data_path, 'rb') as f:
            faces = pickle.load(f)
        faces = np.append(faces, faces_data, axis=0)
        with open(faces_data_path, 'wb') as f:
            pickle.dump(faces, f)

    return True

# Streamlit UI
st.title('Student Registration')

student_id = st.text_input("Enter Your Student ID (e.g., 100943851)")
email = st.text_input("Enter Your Email")
first_name = st.text_input("Enter Your First Name")
last_name = st.text_input("Enter Your Last Name")
year_of_study = st.number_input("Enter Your Year of Study", min_value=1, max_value=4, step=1)
password = st.text_input("Enter Your Password", type="password")

# Multi-select menu for courses
courses = st.multiselect("Select Your Courses", ['AI Enterprise', 'Capstone 2', 'Advanced ML'])

if st.button('Register'):
    if not email or not first_name or not last_name or not year_of_study or not password or not student_id:
        st.error("All fields are required")
    elif not courses:
        st.error("At least one course must be selected")
    else:
        # Capture face images
        st.info("Please look at the camera to capture your images")
        captured = capture_images(f"{first_name} {last_name}")

        if captured:
            # Prepare student data
            hashed_password = sha256(password.encode()).hexdigest()
            student_data = {
                "student_id": student_id,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "year_of_study": year_of_study,
                "password": hashed_password,  # Store the hashed password
                "courses": courses
            }

            # Send registration data to API
            response = requests.post(f"{API_URL}/students/", json=student_data)
            if response.status_code == 200:
                st.success("Student registered successfully!")
            else:
                st.error(f"Error: {response.text}")