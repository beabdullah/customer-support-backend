from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.core.db import Base
import enum

class Role(enum.Enum):
    USER = "user"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(Role), default=Role.USER, nullable=False)
    tickets = relationship("Ticket", back_populates="user")