from schema.user_schema import UserProfileResponse,UpdateProfileRequest
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
    def updateUserProfile(self, db: Session, userId: str, updateRequest: UpdateProfileRequest):
        profile = self.authRepo.get_user_profile(db, userId)
        if profile is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        
        updated = self.authRepo.update_user_profile(db, userId, updateRequest.displayName)
        return UserProfileResponse(
            displayName=updated.display_name,
            email=updated.user.email,
            profilePic=updated.profile_picture
        )