from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SettlementBase(BaseModel):
    id: Optional[int] = Field(None, description="The unique identifier of the settlement")
    amount: float = Field(..., description="The amount of the settlement")
    currency: str = Field(..., description="The currency of the settlement")
    status: str = Field(..., description="The status of the settlement")
    created_at: Optional[datetime] = Field(None, description="The timestamp when the settlement was created")
    updated_at: Optional[datetime] = Field(None, description="The timestamp when the settlement was last updated")

    class Config:
        orm_mode = True