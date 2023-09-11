# models.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Table
#from sqlalchemy.ext.declarative import declarative_base
#from config.database import meta, engine, db, Base
from config.database import Base
# Base = declarative_base()


'''person = Table(
    "person",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("phone", String(255))
)'''

#meta.create_all(db)

class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    phone = Column(String(255))