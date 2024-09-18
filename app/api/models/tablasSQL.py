from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base

#llamado a la base para crear tablas
Base=declarative_base()

#definicion de las tablas de mi modelo

#usuario
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    fechaNacimiento=Column(Date)
    ubicacion=(String(100))
    metaAhorro=Column(Float)

class Gastos(Base):
    __tablename__='gastos'
    id=Column(Integer, primary_key=True, autoincrement=True)
    decripcion=Column(String(50))
    categoria=Column(String(50))
    valor=Column(Float)
    fecha=Column(Date)

class Categoria(Base):
    __tablename__='categoria'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    decripcion=Column(String(50))
    fotoCategoria=Column(String(50))

class Ingreso(Base):
    __tablename__='ingreso'
    id=Column(Integer, primary_key=True, autoincrement=True)
    decripcion=Column(String(50))
    valor=Column(Float)
    fecha=Column(Date)


