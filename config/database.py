from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


# URL_DATABASE = "mysql+pymysql://homestead:secret@localhost:3306/BlogApplication"
URL_DATABASE = "postgresql://postgres:secret@pyDev/myblog"
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
