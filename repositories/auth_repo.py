from sqlalchemy.orm import Session
from models.auth_model import  Users, Sessions, UserTypes


class UserRepository:

    def get_all(self, db: Session):
        return db.query(Users).all()

    def get_user_by_username(self,db: Session, username: str):
        return db.query(Users).filter(Users.username == username).first()
    
    def insert_new_user(self, db: Session, user: Users):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user