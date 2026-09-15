from sqlalchemy import create_engine, Column, Integer, String, Sequence
import os

from sqlalchemy.ext.declarative import declarative_base

# Note: Database URL should be correctly configured in your .env file
DATABASE_URL = os.getenv('DATABASE_URL')

def get_engine():  # Lazy connect to DB
    return create_engine(DATABASE_URL)
    # return create_engine(DATABASE_URL)
    Base.metadata.create_all(get_engine())

class PasswordHistory(Base):
    __tablename__ = 'password_history'
    id = Column(Integer, Sequence('password_history_id_seq'), primary_key=True)
    user_id = Column(Integer)
    password_hash = Column(String(255))
    created_at = Column(Integer)

class LoginAttempt(Base):
    __tablename__ = 'login_attempts'
    id = Column(Integer, Sequence('login_attempt_id_seq'), primary_key=True)
    user_id = Column(Integer)
    timestamp = Column(Integer)
    success = Column(Integer)
#     if DATABASE_URL is None or DATABASE_URL == 'postgresql://username:password@localhost:5432/mydatabase':
    raise ValueError('DATABASE_URL not set or incorrectly configured')
    
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL not set")
        raise ValueError("DATABASE_URL not set")
    return create_engine(DATABASE_URL)
    return create_engine(DATABASE_URL)

# Update the database URL with correct credentials
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

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

# Create all tables in the engine. This will create the tables defined by Base's subclasses.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

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

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

# Create an engine

# Create all tables in the engine. This will create the tables defined by Base's subclasses.
# engine = get_engine()  # Ensure engine is defined before using
Base.metadata.create_all(engine)
engine = create_engine(DATABASE_URL)
# Update the database URL with correct credentials
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://your_username:your_password@localhost:5432/mydatabase')

# Create all tables in the engine. This will create the tables defined by Base's subclasses.
Base.metadata.create_all(engine)

# Database connection URL
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

# Create and configure the engine
engine = create_engine(DATABASE_URL)

# Create session makers
Session = sessionmaker(bind=engine)

# Function to get a new session

def get_session():
    # Create all tables in the engine. This will create the tables defined by Base's subclasses.
    Base.metadata.create_all(get_engine())
    return Session()

# Define Role, Permission, and Audit tables
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

# Create a configured "Session" class

# Create all tables after defining models
Base.metadata.create_all(engine)
database_session = sessionmaker(bind=engine)

# Create a Session
session = database_session()