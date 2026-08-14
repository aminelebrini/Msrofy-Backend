from fastapi import APIRouter ,Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.GroupBase import GroupBase , GroupCreate
from app.schemas.GroupMemberBase import GroupMemberAdd
from app.Api.controllers.CreateGroupController import CreateGroupController
from app.Api.controllers.AddMemberToGroupeController import AddMemberToGroupeController
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create-group")
async def create_group(data: GroupCreate, db: Session = Depends(get_db)):
    create_group_controller = CreateGroupController(db)
    return create_group_controller.create_group(data)

@router.post("/add-member")
async def add_member_to_group(data: GroupMemberAdd, db: Session = Depends(get_db)):
    add_member_controller = AddMemberToGroupeController(db)
    return add_member_controller.add_member(data.group_id, data.user_id, data.role)