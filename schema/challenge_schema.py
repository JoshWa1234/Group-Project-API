from pydantic import BaseModel
from typing import Optional


class ChallengeCreateRequest(BaseModel):
    title: str
    description: Optional[str] = None
    points: int
    target: int
    frequency: str
    due_date: str
    assigned_to: str


class ChallengeResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    points: int
    target: int
    frequency: str
    due_date: str
    assigned_to: str
    status: str
    progress: int

    class Config:
        from_attributes = True

class ChallengeProgressUpdateRequest(BaseModel):
    progress: int