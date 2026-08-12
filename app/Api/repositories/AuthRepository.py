from sqlalchemy.orm import Session
from app.models import User

class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def authenticate(self, request):

        user = self.db.query(User).filter(User.email == request.email).first()

        if(user and user.password == request.password):
            return user
        else:
            return None

    def create_user(self, request):
        user = User(
            email=request.email,
            password=request.password
        )
        self.db.add(user)
        self.db.commit()
        if(self.db.refresh(user)):
            return user
        else:
            return None