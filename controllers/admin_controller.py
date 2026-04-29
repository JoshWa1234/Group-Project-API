from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from dependencies import get_admin_session
from services.admin_service import AdminService
from schema.admin_schema import UserAdminView, SessionAdminView, UpdateUserRequest, UserTypeSchema
from typing import List

router = APIRouter(prefix="/admin", tags=["admin"])
service = AdminService()

@router.get("/users", response_model=List[UserAdminView])
def getUsers(db: Session = Depends(get_db), session = Depends(get_admin_session)):
    return service.getUsers(db)

@router.delete("/users/{userId}")
def deleteUser(userId: str, db: Session = Depends(get_db), session = Depends(get_admin_session)):
    return service.deleteUser(db, userId)

@router.get("/sessions", response_model=List[SessionAdminView])
def getSessions(db: Session = Depends(get_db), session = Depends(get_admin_session)):
    return service.getSessions(db)

@router.delete("/sessions/{sessionId}")
def deleteSession(sessionId: str, db: Session = Depends(get_db), session = Depends(get_admin_session)):
    return service.deleteSession(db, sessionId)

@router.put("/users/{userId}", response_model=UserAdminView)
def updateUser(userId: str, updateRequest: UpdateUserRequest,
               db: Session = Depends(get_db),
               session = Depends(get_admin_session)):
    return service.updateUser(db, userId, updateRequest)

@router.get("/user-types", response_model=List[UserTypeSchema])
def getUserTypes(db: Session = Depends(get_db), session = Depends(get_admin_session)):
    return service.getUserTypes(db)