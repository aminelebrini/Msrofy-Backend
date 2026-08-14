from app.Api.repositories.AddMemberToGroupeRepository import AddMemberToGroupeRepository

class AddMemberToGroupeService:
    def __init__(self, db):
        self.db = db
        self.add_member_repository = AddMemberToGroupeRepository(db)

    def add_member(self, group_id, user_id, role):
        return self.add_member_repository.add_member(group_id, user_id, role)