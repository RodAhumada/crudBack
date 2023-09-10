from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    rut:str
    nombre:str
    apPaterno:str
    apMaterno:str
    fono:int
    mail:str
    password:str

class UserId(BaseModel):
	id:int

class ListUser(BaseModel):
    id:int
    rut:str
    nombre:str
    apPaterno:str
    apMaterno:str
    fono:int
    mail:str
    class Config():
        from_attributes = True

class DelUser(BaseModel):
    rut:str
    nombre:str
    apPaterno:str
    apMaterno:str
    class Config():
        from_attributes = True

