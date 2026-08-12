from Api.services.AuthService import AuthService

class AuthController:
    def __init__(self):
        self.auth_service = AuthService()

    def login(self, request):
        return self.auth_service.login(request)

    def register(self, request):
        return self.auth_service.register(request)