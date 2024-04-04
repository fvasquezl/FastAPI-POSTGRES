from typing import List
from pydantic import BaseModel, Field
from schemas.post import Post


# Esquema Pydantic para los usuarios
class UserBase(BaseModel):
    username: str = Field(min_lengt=5, max_lenght=50)
    email: str = Field(min_lengt=5, max_lenght=70)


# Esquema Pydantic para recibir datos de usuario
class UserCreate(UserBase):
    password: str = Field(min_lengt=5, max_lenght=30)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "MyUserName",
                "email": "MyEmail@mydomain.com",
                "password": "MyPassword",
            }
        }


# Esquema Pydantic para devolver datos de usuario
class User(UserBase):
    id: int
    blog_posts: List[Post] = []

    class Config:
        orm_mode = True
