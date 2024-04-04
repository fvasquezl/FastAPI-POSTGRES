from typing import Annotated
from fastapi import APIRouter, Depends
from config.database import SessionLocal

from models import Post as PostModel
from schemas import post as PostSchema


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[SessionLocal, Depends(get_db)]


@router.post("/posts/", response_model=PostSchema.Post)
def create_blog_post(post: PostSchema.PostCreate, db: db_dependency):
    db_post = PostModel(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
