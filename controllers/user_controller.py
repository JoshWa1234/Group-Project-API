from fastapi import APIRouter, Depends, Response, Request, HTTPException

from schema.user_schema import UserProfileResponse
from sqlalchemy.orm import Session
from services.auth_service import AuthService

from database.db import get_db

router = APIRouter(prefix="/user", tags=["authentication"])
service = AuthService()


@router.get("/userProfile/{userID}", response_model=UserProfileResponse)
def userProfile(
    Request: Request,
    userID: str,
    db: Session = Depends(get_db)
):
    session_token = Request.cookies.get("session_token") 
    
    # if not session_token:
    #     raise HTTPException(status_code=401, detail="Not authenticated")
    
    response = UserProfileResponse(
        displayName='Josh',
        email='josh@example.com',
        badgeList=['1','2'],
        pointsLogHistory=['1234', '1', '5', '124']
    )

    return response
    