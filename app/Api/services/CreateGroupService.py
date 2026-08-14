from app.Api.repositories.CreateGroupRepository import CreateGroupRepository

class CreateGroupService:
    def __init__(self, db):
        self.db = db
        self.create_group_repository = CreateGroupRepository(db)

    def create_group(self, group_data):
        return self.create_group_repository.create_group(group_data)
