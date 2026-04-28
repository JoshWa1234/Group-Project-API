from schema.user_schema import UserProfileResponse
from repositories.auth_repo import UserRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException

class UserService:
    authRepo = UserRepository()

    def getUserProfiles(self, db:Session, userId: str):

        user = self.authRepo.get_user_by_id(db, userId)
        userProfile = self.authRepo.get_user_profile(db, userId)

        if userProfile is None:
            raise HTTPException(status_code=404, detail="Profile not found")

        return UserProfileResponse(
            displayName=userProfile.display_name,
            email=user.email,
            profilePic=userProfile.profile_picture,
        )
