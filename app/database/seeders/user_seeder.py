from sqlalchemy.orm import Session
from app.models.User import User
from app.core.security import Security

def seed_users(db: Session):
    users = [
        User(
           username = "admin",
            full_name = "Admin User",
            email = "admin@msrofy.ma",
            password = Security.hash_password("admin1234")
        )
    ]

    db.add_all(users)
    db.commit()