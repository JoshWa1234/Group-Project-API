from utils.auth_utils import verifyPassword, generateAuthToken,hashPassword,validatePassword,gerateNewID
from schema.auth_schema import LoginRequest, LoginResponse, UserSchema, ResetPasswordRequest
from repositories.auth_repo import UserRepository
from sqlalchemy.orm import Session
from fastapi import Response, HTTPException
from config import settings
from models.auth_model import Users
from datetime import datetime
from typing import Any
class AuthService:
    authRepo = UserRepository()

    def login(self, db: Session, loginRequest: LoginRequest, response: Response):
        #check user exists
        user = self.authRepo.get_user_by_username(db, loginRequest.email)
        if user is None:
            return LoginResponse(
                errorMessage="Username or password was incorrect",
                statusCode=401
            )
        #verify password
        if not verifyPassword(loginRequest.password, user.password_hash):
            return LoginResponse(
                errorMessage="Username or password was incorrect",
                statusCode=401
            )
        #set token for sessions
        self.setUpToken(response, user.id, db)

        return LoginResponse(
            user=UserSchema.model_validate(user), # validates against datbase model
            statusCode=200 # success code
        )
    def delete_session(self,db: Session, session_token: Any, response: Response):
        #Deletes database session
        self.authRepo.delete_session(db, session_token)
        #Deletes the HTTP Cookie 
        response.delete_cookie("session_token")
        
        return {"message": "Logged out"}
    
    def setUpToken(self, response: Response, userId: str, db: Session):
        token = generateAuthToken()
        response.set_cookie(
            key="session_token",
            value=token,
            httponly=True,
            secure=settings.environment == 'production',
            samesite="lax",
            max_age=60 * 60
        )
        self.authRepo.save_session(db, userId, token)
        return token
    def signUp(self, db: Session, loginRequest: LoginRequest, response: Response):
        #check user exists
        default_user_type = settings.default_user_type_id

        existing_user = self.authRepo.get_user_by_username(db, loginRequest.email)
        if existing_user:
            return LoginResponse(
                errorMessage="An account with this email already exists",
                statusCode=409
            )

        if not validatePassword(loginRequest.password):
            return LoginResponse(
                errorMessage='User password does not meet minimum security requirments',
                statusCode=422
            )
         
        hashed_pass = hashPassword(loginRequest.password)
        
        newUser = Users(
            id=gerateNewID(),
            username=loginRequest.email,
            user_type_id=default_user_type,
            password_hash=hashed_pass,
            email=loginRequest.email,
            created_at=datetime.now(),
            updated_at=datetime.now()
            )

        self.authRepo.insert_new_user(db,newUser)
        self.authRepo.create_user_profile(db, newUser.id) 
        #set token for sessions
        self.setUpToken(response,newUser.id,db)

        return LoginResponse(
            user=UserSchema.model_validate(newUser),
            statusCode=200
        )
    
    def resetPassword(self, db: Session, userId: str, resetRequest: ResetPasswordRequest):
        user = self.authRepo.get_user_by_id(db, userId)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if not verifyPassword(resetRequest.currentPassword, user.password_hash):
            raise HTTPException(status_code=401, detail="Current password is incorrect")

        newPassword = hashPassword(resetRequest.newPassword)
        self.authRepo.update_password(db, userId,newPassword )
        return {"message": "Password updated successfully"}
    