from fastapi import FastAPI
from .routers import attendance, meetings, auth

app = FastAPI()

app.include_router(attendance.router)
app.include_router(meetings.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Smart Attend Backend is Running"}
