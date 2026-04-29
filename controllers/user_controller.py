from fastapi import APIRouter, Depends, Request, HTTPException

from schema.user_schema import UserProfileResponse,UpdateProfileRequest
from sqlalchemy.orm import Session
from services.user_service import UserService
from dependencies import get_current_session
from database.db import get_db

router = APIRouter(prefix="/user", tags=["authentication"])
service = UserService()


@router.get("/userProfile/{userID}", response_model=UserProfileResponse)
def userProfile(
    Request: Request,
    userID: str,
    db: Session = Depends(get_db),
    session = Depends(get_current_session) # this is an auth gaurd which will throw 401 if failure
):
    session_token = Request.cookies.get("session_token") 

    if not session_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    response = service.getUserProfiles(db,userID)

    return response
    

@router.put("/userProfile/{userID}", response_model=UserProfileResponse)
def updateProfile(
    userID: str,
    updateRequest: UpdateProfileRequest,
    db: Session = Depends(get_db),
    session = Depends(get_current_session)
):
    return service.updateUserProfile(db, userID, updateRequest)