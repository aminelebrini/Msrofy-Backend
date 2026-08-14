from fastapi import APIRouter , Session, Depends
from sqlalchemy.orm import Session
from app.Api.controllers.AuthController import AuthController
from app.database.database import SessionLocal
from app.schemas.UserBase import UserCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
async def login(data: UserCreate, db: Session = Depends(get_db)):
    auth_controller = AuthController(db)
    return auth_controller.login(data)

   

@router.post("/register")
async def register(data: UserCreate, db: Session = Depends(get_db)):
    auth_controller = AuthController(db)
    return auth_controller.register(data)
    