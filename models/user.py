from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    email = Column(String(70), unique=True, index=True)
    password = Column(String(30))

    # Definimos la relación uno a muchos con las publicaciones de blog
    posts = relationship("Post", back_populates="author")
