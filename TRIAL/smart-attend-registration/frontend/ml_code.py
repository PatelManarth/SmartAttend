import cv2
import pickle
import numpy as np

# Load data
with open('data/names.pkl', 'rb') as f:
    names = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
    faces_data = pickle.load(f)

# Train the model
knn = cv2.ml.KNearest_create()
knn.train(faces_data, cv2.ml.ROW_SAMPLE, np.array(names))
