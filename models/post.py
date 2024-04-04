from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    author_id = Column(Integer, ForeignKey("users.id"))

    # Definimos la relación muchos a uno con el usuario autor
    author = relationship("User", back_populates="posts")
