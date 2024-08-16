
# SmartAttend
![SmartAttend System Image](image1.jpeg)
## Overview

SmartAttend is a comprehensive, AI-powered attendance management system designed to automate the process of attendance tracking. The system uses facial recognition technology to track attendance in real-time during Zoom meetings and other virtual classroom settings. This project is split into three main components:

1. **Backend (FastAPI):** Responsible for managing the core logic, APIs, and database interactions.
2. **Frontend (React):** Provides the user interface for faculty and students to interact with the system.
3. **Registration (Streamlit):** Facilitates student registration with face capture functionality.

## Group Members (Collaborators)

- Manarth Patel
- Shriram Yadav
- Rakshay Patel
- Manu Shrivastava

## Project Structure

The project is split into multiple directories, each serving a specific purpose.

### 1. **smart-attend-backend/**
This folder contains the backend logic for the SmartAttend project using FastAPI. It handles CRUD operations, user authentication, attendance, and meeting scheduling.

- **app/** - Contains the main application logic.
  - `crud.py` - CRUD operations.
  - `database.py` - Database connection setup.
  - `main.py` - Main FastAPI application entry point.
  - `models.py` - Database models.
  - `routers/attendance.py` - Attendance-related API routes.
  - `routers/auth.py` - Authentication-related API routes.
  - `routers/meetings.py` - Meeting scheduling and management routes.
  - `utils.py` - Utility functions.
  
- **auth_endpoint/** - Handles user authentication using a separate Node.js service.
  - `.husky/pre-commit` - Pre-commit hooks.
  - `.prettierrc` - Prettier configuration.
  - `src/index.js` - Entry point for the authentication service.

### 2. **smart-attend-frontend/**
This folder contains the React frontend application that serves as the user interface for students and faculty.

- **frontend/** - Core React application.
  - `App.jsx` - Main application file.
  - `components/AdminPortal.jsx` - Faculty admin portal.
  - `components/Attendance.jsx` - Attendance tracking component.
  - `components/FacultyHome.jsx` - Faculty homepage.
  - `components/MeetingScheduler.jsx` - Meeting scheduling component.
  - `components/StudentHome.jsx` - Student homepage.
  - `components/VideoGrid.js` - Video stream grid for Zoom meetings.

### 3. **smart-attend-registration/**
This folder contains the Streamlit-based registration system, along with facial recognition and machine learning code.

- **frontend/** - Contains the Streamlit frontend for registration.
  - `add_face.py` - Script to add a new face for recognition.
  - `app.py` - Main Streamlit app file.
  - `data/` - Contains trained models and data files (`faces_data.pkl`, `names.pkl`).
  - `ml_code.py` - Machine learning code for face recognition.
  - `utils.py` - Utility functions.
  
- **backend/** - Backend FastAPI code for registration-related APIs.
  - `crud.py` - CRUD operations for registration.
  - `database.py` - Database connection setup.
  - `main.py` - Main FastAPI application for registration.
  - `models.py` - Database models.

### 4. **TRIAL/**
This folder is used to experiment with new features and functionalities before integrating them into the main project.

## GitHub Repository

You can access the project's GitHub repository [here](https://github.com/PatelManarth/SmartAttend.git).

### Cloning the Repository with Submodules

To clone the repository along with its submodules, use the following command:

```bash
git clone --recurse-submodules https://github.com/PatelManarth/SmartAttend.git
```

If you've already cloned the repository without submodules, you can initialize and update the submodules with:

```bash
git submodule update --init --recursive
```

## Setup Guide

This guide will help you set up and run the project on your local machine. The project is divided into three main parts, each with its own setup instructions.

### Prerequisites

- Python 3.8+
- Node.js
- npm or yarn
- MongoDB
- Zoom SDK (for video stream integration)
- Git

### Backend (FastAPI)

1. **Navigate to the backend directory:**
   ```bash
   cd smart-attend-backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file with your database credentials and other environment variables.

4. **Run the FastAPI application:**
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend (React)

1. **Navigate to the frontend directory:**
   ```bash
   cd smart-attend-frontend/frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the React application:**
   ```bash
   npm start
   ```

### Registration (Streamlit)

1. **Navigate to the registration directory:**
   ```bash
   cd smart-attend-registration/frontend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

## Deployment

To deploy this project, consider using services like AWS (EC2, S3), Heroku, or any other cloud provider that supports Python and Node.js applications. Ensure that the environment is properly set up for MongoDB, and configure the Zoom SDK for video stream processing.

## License

This project is licensed under the MIT License. See the [LICENSE.md](smart-attend-backend/auth_endpoint/LICENSE.md) file for details.

## Contributions

We welcome contributions! Please see the [CONTRIBUTING.md](smart-attend-backend/auth_endpoint/CONTRIBUTING.md) file for more information.

---

For any questions or additional help, feel free to contact any of the project collaborators.
