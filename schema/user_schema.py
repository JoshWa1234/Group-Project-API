from pydantic import BaseModel
from typing import Optional, List

class UserProfileResponse(BaseModel):
    displayName: str
    email: str
    badgeList: List = []
    pointsLogHistory: List = []