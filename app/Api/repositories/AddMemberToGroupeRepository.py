from sqlalchemy.orm import Session
from app.models.GroupMember import GroupMember

class AddMemberToGroupeRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_member(self, group_id, user_id):
        new_member = GroupMember(group_id=group_id, user_id=user_id, role="member")
        self.db.add(new_member)
        self.db.commit()
        self.db.refresh(new_member)
        return new_member