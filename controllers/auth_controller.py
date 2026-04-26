from fastapi import APIRouter, Depends, Response
from schema.auth_schema import LoginResponse, LoginRequest
from sqlalchemy.orm import Session
from services.auth_service import AuthService
from database.db import get_db

router = APIRouter(prefix="/auth", tags=["authentication"])
service = AuthService()

@router.post("/login", response_model=LoginResponse)
def login(
    loginRequest: LoginRequest,
    response: Response,
    db: Session = Depends(get_db)
):
    result = service.login(db, loginRequest, response)
    return result

@router.post("/sign_up")
def createUser(
    loginRequest: LoginRequest,
    response: Response,
    db: Session = Depends(get_db)
    ):
    result = service.signUp(db, loginRequest, response)
    return result