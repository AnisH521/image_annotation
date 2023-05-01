import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String, Integer, Float, Text, LargeBinary
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class img_db(Base):
    __tablename__ = "image_database"
    id = Column(Integer, primary_key = True)
    name = Column(Text, nullable = True)
    img = Column(LargeBinary, unique = False, nullable = False)  
