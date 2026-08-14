from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional 

class GroupBase(BaseModel):
    id: Optional[int] = Field(None, description="The unique identifier of the group")
    name: str = Field(..., description="The name of the group")
    description: Optional[str] = Field(None, description="The description of the group")
    created_at: Optional[datetime] = Field(None, description="The timestamp when the group was created")
    updated_at: Optional[datetime] = Field(None, description="The timestamp when the group was last updated")

    class Config:
        orm_mode = True

class GroupCreate(GroupBase):
    owner_id: int = Field(..., description="The ID of the user who owns the group")

class GroupResponse(GroupBase):
    id: int
    created_at: datetime