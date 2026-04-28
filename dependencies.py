from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from repositories.auth_repo import UserRepository

authRepo = UserRepository()

def get_current_session(request: Request, db: Session = Depends(get_db)):
    session_token = request.cookies.get("session_token")

    if not session_token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    session = authRepo.get_session_by_token(db, session_token)
    if not session:
        raise HTTPException(status_code=401, detail="Invalid or expired session")

    return session