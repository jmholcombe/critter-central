from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Request model for user login
class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    # Dummy authentication logic (replace with real authentication later)
    if request.email == "test@example.com" and request.password == "password123":
        return {"message": "Login successful", "email": request.email}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")
