from fastapi import APIRouter, Depends, Response
from schema.auth_schema import LoginResponse, LoginRequest
from sqlalchemy.orm import Session
from services.auth_service import AuthService
from database.db import get_db
from dependencies import get_current_session

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

@router.post("/logout")
def logout(response: Response,
            db: Session = Depends(get_db), 
            session = Depends(get_current_session) # Auth Gaurd
            ):
    response = service.delete_session(db, session.session_token, response)
    return response