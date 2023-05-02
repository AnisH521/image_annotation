import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String, Integer, Float, Text, LargeBinary
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class img_db(Base):
    __tablename__ = "image_database"
    id = Column(Integer, primary_key = True)
    user_name = Column(Text, nullable = False)
    file_name = Column(Text, nullable = False)
    img = Column(LargeBinary, unique = False, nullable = False)

#engine = create_engine("sqlite:///image_db.sqlite3")
#Base.metadata.create_all(engine)
