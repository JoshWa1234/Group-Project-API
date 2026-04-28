from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    app_name: str = "WorkPlace Wellness"
    admin_email: str = ""
    items_per_user: int = 50
    default_user_type_id:int = 2
    environment: Literal['production', 'dev'] = 'dev'

settings = Settings()