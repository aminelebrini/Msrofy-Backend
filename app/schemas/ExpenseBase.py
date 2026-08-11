from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ExpenseBase(BaseModel):
    id: Optional[int] = Field(None, description="The unique identifier of the expense")
    amount: float = Field(..., description="The amount of the expense")
    currency: str = Field(..., description="The currency of the expense")
    description: Optional[str] = Field(None, description="The description of the expense")
    created_at: Optional[datetime] = Field(None, description="The timestamp when the expense was created")
    updated_at: Optional[datetime] = Field(None, description="The timestamp when the expense was last updated")

    class Config:
        orm_mode = True

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int
    created_at: datetime