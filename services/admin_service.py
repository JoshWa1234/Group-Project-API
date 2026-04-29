from repositories.auth_repo import UserRepository
from schema.admin_schema import UpdateUserRequest
from sqlalchemy.orm import Session
from fastapi import HTTPException

class AdminService:
    repo = UserRepository()

    def getUsers(self, db: Session):
        return self.repo.get_all(db)

    def deleteUser(self, db: Session, userId: str):
        user = self.repo.get_user_by_id(db, userId)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        self.repo.delete_user(db, userId)
        return {"message": "User deleted"}

    def getSessions(self, db: Session):
        return self.repo.get_all_sessions(db)

    def deleteSession(self, db: Session, sessionId: str):
        self.repo.delete_session_by_id(db, sessionId)
        return {"message": "Session deleted"}

    def updateUser(self, db: Session, userId: str, updateRequest: UpdateUserRequest):
        user = self.repo.get_user_by_id(db, userId)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repo.update_user(db, userId, updateRequest)

    def getUserTypes(self, db: Session):
        return self.repo.get_all_user_types(db)