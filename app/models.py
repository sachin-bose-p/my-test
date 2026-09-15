from sqlalchemy import Column, Integer, String, Sequence
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(255))  # Increased to accommodate hashed password

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(255))  # Increased to accommodate hashed password

class UserSession(Base):
    __tablename__ = 'user_sessions'
    id = Column(Integer, Sequence('user_session_id_seq'), primary_key=True)
    user_id = Column(Integer)
    session_token = Column(String(255))
    expiration = Column(Integer)

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