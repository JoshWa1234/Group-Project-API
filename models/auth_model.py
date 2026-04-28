from database.db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class UserTypes(Base):
    __tablename__ = "user_types"
    id = Column(String, nullable=False, primary_key=True)
    name = Column(String)

class Users(Base):
    __tablename__ = "users"
    id = Column(String, nullable=False, primary_key=True)
    email = Column(String, nullable=True)
    password_hash = Column(String)
    username = Column(String)
    user_type_id = Column(String, ForeignKey("user_types.id"))  
    user_type = relationship("UserTypes")                       
    created_at = Column(DateTime)                               
    updated_at = Column(DateTime)                               

class Sessions(Base):
    __tablename__ = "sessions"
    id = Column(String, nullable=False, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))             
    user = relationship("Users")                                 
    session_token = Column(String)
    expires_at = Column(DateTime)
    created_at = Column(DateTime)

class UserProfie(Base):
    __tablename__ = "user_profile"
    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))                                             
    display_name = Column(String)
    profile_picture = Column(String)
    updated_at = Column(DateTime)

