from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class GroupMemberBase(BaseModel):
    id: Optional[int] = Field(None, description="The unique identifier of the group member")
    user_id: int = Field(..., description="The ID of the user")
    group_id: int = Field(..., description="The ID of the group")
    role: str = Field(..., description="The role of the user in the group (e.g., 'admin', 'member')")
    created_at: Optional[datetime] = Field(None, description="The timestamp when the group member was created")
    updated_at: Optional[datetime] = Field(None, description="The timestamp when the group member was last updated")

    class Config:
        orm_mode = True

class GroupMemberAdd(GroupMemberBase):
    pass