from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ExpenseSplitBase(BaseModel):
    id: Optional[int] = Field(None, description="The unique identifier of the expense split")
    expense_id: int = Field(..., description="The ID of the expense")
    user_id: int = Field(..., description="The ID of the user")
    amount: float = Field(..., description="The amount of the expense split")
    created_at: Optional[datetime] = Field(None, description="The timestamp when the expense split was created")
    updated_at: Optional[datetime] = Field(None, description="The timestamp when the expense split was last updated")

    class Config:
        orm_mode = True