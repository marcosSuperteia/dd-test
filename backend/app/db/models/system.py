import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, Text
from sqlalchemy.orm import relationship

class System(Base):
    __tablename__ = 'dd_system'

    id = Column(Integer, primary_key=True, autoincrement=True)
    SystemName = Column(String(255), nullable=False)
    SystemPrefix = Column(String(3), nullable=True, comment="Prefixo com até 3 letras que será adicionado na criação das tabelas deste sistema.")
    Description = Column(Text, nullable=True)
    CustomerID = Column(Integer, nullable=True)
    data_entry_order = Column(Text, nullable=False, comment="DATA Entry order to ensure that the data modeling and structure will succeed, aligning the functionalities and interactions needed for the system.")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
