from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..database import get_user_by_username
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginRequest(BaseModel):
    username: str
    password: str
    role: str

class LoginResponse(BaseModel):
    success: bool

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    user = get_user_by_username(request.username)
    if user is None or not verify_password(request.password, user["password"]) or user["user_type"] != request.role:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return LoginResponse(success=True)

@router.get("/profile")
async def get_profile(username: str):
    user = get_user_by_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user["username"], "name": user["name"], "role": user["user_type"]}
