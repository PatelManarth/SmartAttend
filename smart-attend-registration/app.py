from flask import Flask, render_template, jsonify, request, Response
from flask_cors import CORS
from focus import gen_frames, capture_images
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['attendance']
students_collection = db['students']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture_images', methods=['GET'])
def capture_images_route():
    captured_images = capture_images()
    return jsonify({"message": "Images captured successfully", "images": captured_images})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    student_id = data['student_id']
    image_folder = f'images/{student_id}'
    
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    captured_images = capture_images()
    for idx, image in enumerate(captured_images):
        # Move images to the designated folder
        os.rename(image, os.path.join(image_folder, f'image_{idx + 1}.jpg'))

    students_collection.insert_one({"student_id": student_id, "image_folder": image_folder})
    return jsonify({"message": "Student registered successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
