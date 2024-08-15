from fastapi import FastAPI
from .routers import students, attendance

app = FastAPI()

app.include_router(students.router)
app.include_router(attendance.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Attend API"}
