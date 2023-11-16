from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(250))
    saldo_deuda = Column(Float, default=0.0)
    

# Configuración de la base de datos Oracle
engine_oracle = create_engine('oracle+cx_oracle://system:12345@172.17.0.2:1522/?service_name=service_name')
# Configuración de la base de datos MySQL
engine_mysql = create_engine('mysql+pymysql://root:23456@localhost/myqsl.bastion')

SessionLocalOracle = sessionmaker(autocommit=False, autoflush=False, bind=engine_oracle)
SessionLocalMySQL = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql)

Base.metadata.create_all(bind=engine_oracle)
Base.metadata.create_all(bind=engine_mysql)
