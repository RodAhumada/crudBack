from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from typing import List

from app.schemas import User, ListUser

from app.db.database import get_db

from app.db import models

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

# *listar usuarios
@router.get('/', response_model=List[ListUser])
def listar_usuarios(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    return data

# *crear usuario
@router.post('/')
def crear_usuario(user:User, db:Session = Depends(get_db)):
    try:
        usuario = user.model_dump()
        nuevo_usuario = models.User(
            rut = usuario["rut"],
            nombre = usuario["nombre"],
            apPaterno = usuario["apPaterno"],
            apMaterno = usuario["apMaterno"],
            fono = usuario["fono"],
            mail = usuario["mail"],
            password = usuario["password"],
        )
        # agregamos el nuevo usuario
        db.add(nuevo_usuario)
        # relizamos el commit
        db.commit()
        # actualizamos
        db.refresh(nuevo_usuario)
        return {"mensaje":"Usuario creado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {str(e)}")