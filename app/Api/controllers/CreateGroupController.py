from app.Api.services.CreateGroupService import CreateGroupService

class CreateGroupController:
    def __init__(self, db):
        self.db = db
        self.create_group_service = CreateGroupService(db)

    def create_group(self, group_data):
        return self.create_group_service.create_group(group_data)