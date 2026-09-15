from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, Sequence('role_id_seq'), primary_key=True)
    role_name = Column(String(50), unique=True)

class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, Sequence('permission_id_seq'), primary_key=True)
    permission_name = Column(String(50), unique=True)

class Audit(Base):
    __tablename__ = 'audit'
    id = Column(Integer, Sequence('audit_id_seq'), primary_key=True)
    action = Column(String(255))

DATABASE_URL = "postgresql://username:password@localhost:5432/mydatabase"

# Create an engine
engine = create_engine(DATABASE_URL)

# Create all tables in the engine. This will create the tables defined by Base's subclasses.
Base.metadata.create_all(engine)

# Create a configured "Session" class
database_session = sessionmaker(bind=engine)

# Create a Session
session = database_session()