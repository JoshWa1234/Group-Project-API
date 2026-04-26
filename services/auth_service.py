from utils.auth_utils import verifyPassword, generateAuthToken,hashPassword,validatePassword,gerateNewID
from schema.auth_schema import LoginRequest, LoginResponse, UserSchema
from repositories.auth_repo import UserRepository
from sqlalchemy.orm import Session
from fastapi import Response
from config import settings
from models.auth_model import Users
from datetime import datetime
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
        self.setUpToken(response)

        return LoginResponse(
            user=UserSchema.model_validate(user),
            statusCode=200
        )
    def setUpToken(self, response: Response):
        token = generateAuthToken()
        response.set_cookie(
            key="session_token",
            value=token,
            httponly=True,
            secure=True,
            samesite="lax",
            max_age=60 * 60
        )
        return token
    def signUp(self, db: Session, loginRequest: LoginRequest, response: Response):
        #check user exists
        default_user_type = settings.default_user_type_id

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

        #set token for sessions
        self.setUpToken(response)

        return LoginResponse(
            user=UserSchema.model_validate(newUser),
            statusCode=200
        )