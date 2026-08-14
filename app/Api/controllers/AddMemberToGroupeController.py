from app.Api.services.AddMemberToGroupeService import AddMemberToGroupeService

class AddMemberToGroupeController:
    def __init__(self, db):
        self.db = db
        self.add_member_service = AddMemberToGroupeService(db)

    def add_member(self, group_id, user_id, role):
        return self.add_member_service.add_member(group_id, user_id, role)