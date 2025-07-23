from sqlalchemy.orm import Session
from schemas import UserCreate, User
from models import User as UserModel # Import your database model
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_user(user: UserCreate, db: Session):
    hashed_password = pwd_context.hash(user.password)
    db_user = UserModel(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return User.from_orm(db_user)
