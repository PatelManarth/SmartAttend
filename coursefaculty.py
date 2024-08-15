from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access the database
db = client["college"]

# Define the faculty details for each course
faculty_data = [
    {"course": "AI Enterprise", "faculty_name": "Manarth Patel", "email": "manarthpatel237@gmail.com"},
    {"course": "Capstone 2", "faculty_name": "Shriram Yadav", "email": "yadavshriram002@gmail.com"},
    {"course": "Advanced ML", "faculty_name": "Rakshay Patel", "email": "rakshay37@gmail.com"}
]

# Create a collection for courses and faculty details
faculty_collection = db["faculty"]

# Insert the faculty data into the collection
result = faculty_collection.insert_many(faculty_data)

# Output the inserted IDs
print("Inserted document IDs:", result.inserted_ids)
