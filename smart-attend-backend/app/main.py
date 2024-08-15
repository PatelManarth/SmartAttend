from fastapi import FastAPI
from .routers import attendance, meetings, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(attendance.router)
app.include_router(meetings.router)
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (POST, GET, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Smart Attend Backend is Running"}
