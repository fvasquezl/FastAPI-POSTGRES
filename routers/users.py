from typing import Annotated
from fastapi import APIRouter, Depends
from config.database import SessionLocal

from models import User as UserModel
from schemas import user as UserSchema


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[SessionLocal, Depends(get_db)]


@router.post("/users/", response_model=UserSchema.User)
async def create_user(user: UserSchema.UserCreate, db: db_dependency):  # type: ignore
    db_user = UserModel(
        username=user.username, email=user.email, password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
