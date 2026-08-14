from app.Api.repositories.AuthRepository import AuthRepository

class AuthService:
    def __init__(self, db):
        self.db = db
        self.auth_repository = AuthRepository(db)

    def login(self, request):

        return self.auth_repository.authenticate(request)

    def register(self, request):

        return self.auth_repository.create_user(request)
