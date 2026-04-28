from sqlalchemy.orm import Session
from models.auth_model import  Users,UserProfie,Sessions
import uuid
from datetime import datetime, timedelta, timezone

class UserRepository:

    def get_all(self, db: Session):
        return db.query(Users).all()

    def get_user_by_username(self,db: Session, username: str):
        return db.query(Users).filter(Users.username == username).first()
    
    def get_user_by_id(self,db: Session, id: str):
        return db.query(Users).filter(Users.id == id).first()
    
    def insert_new_user(self, db: Session, user: Users):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def get_user_profile(self,db: Session, id: str):
        return db.query(UserProfie).filter(UserProfie.user_id == id).first()
    
    def save_session(self, db: Session, userId: str, token: str):
        session = Sessions(
            id=str(uuid.uuid4()),
            user_id=userId,
            session_token=token,
            created_at=datetime.now(timezone.utc),
            expires_at=datetime.now(timezone.utc) + timedelta(hours=1)
        )
        db.add(session)
        db.commit()

    def get_session_by_token(self, db: Session, token: str):
        return db.query(Sessions).filter(
            Sessions.session_token == token,
            Sessions.expires_at > datetime.now(timezone.utc)
        ).first()
    
    def delete_session(self, db: Session, token: str):
        db.query(Sessions).filter(Sessions.session_token == token).delete()
        db.commit()