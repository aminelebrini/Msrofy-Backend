from sqlalchemy.orm import Session
from app.models.Group import Group
from app.models.GroupMember import GroupMember

class CreateGroupRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_group(self, group_data):
        new_group = Group(**group_data)
        self.db.add(new_group)
        self.db.commit()

        if(self.db.refresh(new_group)):
            group_member = GroupMember(group_id=new_group.id, user_id=group_data['owner_id'], role='admin')
            self.db.add(group_member)
            self.db.commit()