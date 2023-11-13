import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer
from sqlalchemy.orm import relationship


class Entity(Base):
    __tablename__ = "dd_entity"
    """
    Database Model for an application user
    """
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    EntityName = Column(String(255), index=True)
    Description = Column(String(255), index=True)
    SystemID = Column(Integer, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )