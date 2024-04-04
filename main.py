from fastapi import FastAPI
from config.database import engine, Base

# from .user import User
# from .post import Post
from routers import users, posts


app = FastAPI()
app.include_router(users.router, prefix="/api")
app.include_router(posts.router, prefix="/api")


Base.metadata.create_all(bind=engine)


# @app.post("/posts/", status_code=status.HTTP_201_CREATED)
# async def create_post(post: PostBase, db: db_dependency):
#     db_post = models.Post(**post.model_dump())
#     db.add(db_post)
#     db.commit()


# @app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
# async def read_post(post_id: int, db: db_dependency):
#     post = db.query(models.Post).filter(models.Post.id == post_id).first()
#     if post is None:
#         raise HTTPException(status_code=404, detail="post not found")
#     return post


# @app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
# async def delete_post(post_id: int, db: db_dependency):
#     db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="post not found")
#     db.delete(db_post)
#     db.commit()


# @app.post("/users/", status_code=status.HTTP_201_CREATED)
# async def create_user(user: UserBase, db: db_dependency):
#     db_user = models.User(**user.model_dump())
#     db.add(db_user)
#     db.commit()


# @app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
# async def read_user(user_id: int, db: db_dependency):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# {
#   "username": "fvasquez",
#   "email": "fvasquez@local.com",
#   "password": "123456"
# }
