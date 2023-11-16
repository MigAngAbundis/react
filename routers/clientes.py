from fastapi import APIRouter, HTTPException, status, Generator, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(
    prefix="/clientes",
    tags=["clientes"]
)

# Dependencia
def get_db():
    db = database.SessionLocalMySQL()
    try:
        yield db
    finally:
        db.close()


# Dependencia para Oracle
def get_db_oracle() -> Generator:
    db = database.SessionLocalOracle()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Cliente, status_code=status.HTTP_201_CREATED)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    nuevo_cliente = models.Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

@router.get("/", response_model=List[schemas.Cliente])
def read_clientes(db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).all()
    return clientes


@router.get("/sucursal_a")
def read_clientes_sucursal_a(db: Session = Depends(get_db_oracle)):
    clientes = db.query(models.Cliente).all()
    return clientes

@router.get("/sucursal_b")
def read_clientes_sucursal_b(db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).all()
    return clientes

@router.get("/todos")
def read_clientes_todos(db_oracle: Session = Depends(get_db_oracle), db_mysql: Session = Depends(get_db)):
    clientes_oracle = db_oracle.query(models.Cliente).all()
    clientes_mysql = db_mysql.query(models.Cliente).all()
    return clientes_oracle + clientes_mysql
