from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Settlement(Base):
    __tablename__ = "settlements"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    payer_id = Column(Integer, ForeignKey("users.id"), nullable=False)    # Debtor paying back
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False) # Creditor receiving
    amount = Column(Float, nullable=False)
    settled_at = Column(DateTime(timezone=True), server_default=func.now())