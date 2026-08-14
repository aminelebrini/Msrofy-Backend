from app.Api.services.AuthService import AuthService

class AuthController:
    def __init__(self, db):
        self.db = db
        self.auth_service = AuthService(db)

    def login(self, request):
        return self.auth_service.login(request)

    def register(self, request):
        return self.auth_service.register(request)
