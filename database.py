from sqlalchemy import create_engine, Column, Integer, String, Sequence
import os

from sqlalchemy.ext.declarative import declarative_base

# Note: Database URL should be correctly configured in your .env file
DATABASE_URL = os.getenv('DATABASE_URL')

def get_engine():  # Lazy connect to DB
    if DATABASE_URL is None or DATABASE_URL == 'postgresql://username:password@localhost:5432/mydatabase':
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
engine = get_engine()  # Ensure engine is defined before using
Base.metadata.create_all(engine)
engine = create_engine(DATABASE_URL)
# Update the database URL with correct credentials
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://your_username:your_password@localhost:5432/mydatabase')

# Create all tables in the engine. This will create the tables defined by Base's subclasses.
Base.metadata.create_all(engine)

    class UserProfiles(Base):
__tablename__ = 'user_profiles'
    __tablename__ = 'user_profiles'
    id = Column(Integer, Sequence('user_profile_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(15))
    country = Column(String(50))
    timezone = Column(String(50))
    currency = Column(String(10))
    profile_image = Column(String(255))  # URL for user's profile image

    def __repr__(self):
        return f'<UserProfiles(id={self.id}, first_name={self.first_name}, last_name={self.last_name})>'
    __tablename__ = 'user_profiles'
    id = Column(Integer, Sequence('user_profile_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(15))
    country = Column(String(50))
    timezone = Column(String(50))
    currency = Column(String(10))
    profile_image = Column(String(255))

    def __repr__(self):
        return f'<UserProfiles(id={self.id}, first_name={self.first_name}, last_name={self.last_name})>'
    __tablename__ = 'user_profiles'
    id = Column(Integer, Sequence('user_profile_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(15))
    country = Column(String(50))
    timezone = Column(String(50))
    currency = Column(String(10))
    profile_image = Column(String(255)) # URL for user's profile image
    __tablename__ = 'user_profiles'
    id = Column(Integer, Sequence('user_profile_id_seq'), primary_key=True);
    first_name = Column(String(50));
    last_name = Column(String(50));
    phone = Column(String(15));
    country = Column(String(50));
    timezone = Column(String(50));
    currency = Column(String(10));
    profile_image = Column(String(255));
    __tablename__ = 'user_profiles'
    id = Column(Integer, Sequence('user_profile_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(15))
    country = Column(String(50))
    timezone = Column(String(50))
    currency = Column(String(10))
    profile_image = Column(String(255))
    __tablename__ = 'user_profiles'
    id = Column(Integer, Sequence('user_profile_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(15))
    country = Column(String(50))
    timezone = Column(String(50))
    currency = Column(String(10))
    profile_image = Column(String(255))
    __tablename__ = 'user_profiles'
    id = Column(Integer, Sequence('user_profile_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(15))
    country = Column(String(50))
    timezone = Column(String(50))
    currency = Column(String(10))
    profile_image = Column(String(255)) # Image URL (path)
    __tablename__ = 'user_profiles'
    id = Column(Integer, Sequence('user_profile_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(15))
    country = Column(String(50))
    timezone = Column(String(50))
    currency = Column(String(10))
    profile_image = Column(String(255))

# Informational comment: make sure the database URL is set in the environment.
# Also, please avoid hard-coding database credentials.

# Create all tables in the engine. This will create the tables defined by Base's subclasses.
Base.metadata.create_all(get_engine())
    __tablename__ = 'user_profiles'
    id = Column(Integer, Sequence('user_profile_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(15))
    country = Column(String(50))
    timezone = Column(String(50))
    currency = Column(String(10))
    profile_image = Column(String(255))

# Database connection URL
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

# Create and configure the engine
engine = create_engine(DATABASE_URL)

# Create session makers
# Removed duplicate UserProfiles class
Session = sessionmaker(bind=engine)

# Function to get a new session

def get_session():
    Base.metadata.create_all(get_engine())
    return Session()
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