# schema/admin_schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserAdminView(BaseModel):
    id: str
    username: str
    email: str
    user_type_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    model_config = {"from_attributes": True}

class SessionAdminView(BaseModel):
    id: str
    user_id: str
    expires_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    model_config = {"from_attributes": True}

class UpdateUserRequest(BaseModel):
    username: str
    email: str
    user_type_id: int

class UserTypeSchema(BaseModel):
    id: int
    name: str
    model_config = {"from_attributes": True}
