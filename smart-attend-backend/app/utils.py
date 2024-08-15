import cv2
import pickle
import numpy as np
import os
import csv
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier

def process_attendance_from_video(video_path):
    facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    with open('data/names.pkl', 'rb') as w:
        LABELS = pickle.load(w)
    with open('data/faces_data.pkl', 'rb') as f:
        FACES = pickle.load(f)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(FACES, LABELS)

    video = cv2.VideoCapture(video_path)
    COL_NAMES = ['NAME', 'TIME']

    while True:
        ret, frame = video.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            crop_img = frame[y:y + h, x:x + w, :]
            resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
            output = knn.predict(resized_img)
            ts = time.time()
            date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
            timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
            attendance = [str(output[0]), str(timestamp)]
            file_path = f"Attendance/Attendance_{date}.csv"
            if not os.path.exists("Attendance"):
                os.makedirs("Attendance")
            if os.path.isfile(file_path):
                with open(file_path, "a", newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(attendance)
            else:
                with open(file_path, "a", newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    writer.writerow(attendance)

    video.release()
    cv2.destroyAllWindows()
