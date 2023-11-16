from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    direccion: str | None = None
    saldo_deuda: float | None = 0.0

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True

