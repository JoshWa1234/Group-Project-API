from pydantic import BaseModel
from typing import List

class UserProfileResponse(BaseModel):
    displayName: str
    email: str
    profilePic: str
    badgeList: List = []
    pointsLogHistory: List = []

class UserProfile(BaseModel):
    id: str

    model_config = {"from_attributes": True}

class UpdateProfileRequest(BaseModel):
    displayName: str