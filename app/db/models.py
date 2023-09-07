from app.db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__= "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rut= Column(String, unique=True)
    nombre= Column(String)
    apPaterno= Column(String)
    apMaterno= Column(String)
    fono= Column(Integer)
    mail= Column(String, unique=True)
    password= Column(String)