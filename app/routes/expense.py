from fastapi import APIRouter ,Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.ExpenseBase import ExpenseCreate
from Api.controllers.AddExpenseController import AddExpenseController

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add-expense")
async def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    add_expense_controller = AddExpenseController(db)
    return add_expense_controller.add_expense(expense.payer, expense.group_id, expense.title, expense.totalAmount)