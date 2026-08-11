from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    id: Optional[int] = Field(None, description="The unique identifier of the user")
    username: str = Field(..., description="The username of the user")
    email: str = Field(..., description="The email address of the user")
    created_at: Optional[datetime] = Field(None, description="The timestamp when the user was created")
    updated_at: Optional[datetime] = Field(None, description="The timestamp when the user was last updated")

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime