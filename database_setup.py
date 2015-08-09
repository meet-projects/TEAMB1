from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'Recipes'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    ingr = Column(String)
    how_to = Column(String)
    type_of = Column(String)
    origin = Column(String)
    story = Column(String)	
    photo = Column(String)

