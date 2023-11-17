import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, Enum, DECIMAL

class UIElement(Base):
    __tablename__ = "dd_uielement"
    """
    Database Model for an application user
    """
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    EntityID = Column(Integer, index=True)
    ElementType = Column(Enum('Label', 'Input Field', 'Text Area', 'Checkbox', 'Radio Button', 'Dropdown', 'Date Picker', 'Time Picker', 'File Upload', 'Image', 'Icon', 'Link', 'Tooltip', 'Slider', name='tipodeelemento'), index=True)
    ElementName = Column(String(255), index=True)
    ElementDescription = Column(String(255), index=True)
    TypingMask = Column(String(255), index=True)
    ValidationRules = Column(String(255), index=True)
    SystemID = Column(Integer, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )