from sqlalchemy import create_engine, Column, Integer, String, Sequence
import os

# To handle logging warnings
import logging

from sqlalchemy.ext.declarative import declarative_base

# Note: Database URL should be correctly configured in your .env file
DATABASE_URL = os.getenv('DATABASE_URL')

def get_engine():  # Lazy connect to DB
    # Set a default database URL for development/testing
    default_url = 'postgresql://username:password@localhost:5432/mydatabase'
    if not DATABASE_URL or DATABASE_URL == default_url:
        logging.warning("DATABASE_URL not set or using the development default. Override this in production.")
        return create_engine(default_url)

    return create_engine(DATABASE_URL)

# Update the database URL with correct credentials
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

# Removed duplicate Role class definition

# Removed duplicate Permission and Audit class definitions

# Create all tables in the engine. This will create the tables defined by Base's subclasses.


DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

# Create session makers and functions to interact with the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker()

# Function to get a new session

def get_session():
    db_engine = get_engine()
    Session.configure(bind=db_engine)  # Bind sessionmaker to the engine
    Base.metadata.create_all(db_engine)  # Create all tables
    return Session()

# Removed duplicate Role class definition

class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, Sequence('permission_id_seq'), primary_key=True)
    permission_name = Column(String(50), unique=True)

class Audit(Base):
    __tablename__ = 'audit'
    id = Column(Integer, Sequence('audit_id_seq'), primary_key=True)
    action = Column(String(255))

# Function to provide a database session

def get_db():
    db = None
    try:
        db = get_session()
        yield db
    finally:
        if db:
            db.close()

# Create a configured "Session" class

