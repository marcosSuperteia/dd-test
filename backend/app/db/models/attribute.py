import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, Enum, DECIMAL


class Attribute(Base):
    __tablename__ = "dd_attribute"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    EntityID = Column(Integer, nullable=True)
    AttributeName = Column(String(255), nullable=False)
    DataType = Column(Enum('Integer', 'Float', 'String', 'Date', 'Time', 'DateTime', 'Boolean', 'Currency', 'Email', 'URL', 'Phone Number', 'Address', 'Image', 'File', 'Password', name='datatype'), nullable=True)
    size = Column(DECIMAL(7, 0), nullable=True, server_default='0', comment='Tamanho do Atributo')
    label = Column(String(100), nullable=True, comment='Label que será utilizado na montagem das Telas.\r\nCaso omitido o nome do Atributo será utilizado.')
    tooltip = Column(String(250), nullable=True, comment='Texto sintético a ser utilizado no preenchimento automático do Tooltip quando o usuário estiver com o Mouse sobre o campo.')
    help = Column(String, nullable=True, comment='Texto / HTML descritivo - que será utilizado para montagem do HELP do Sistema')
    IsRequired = Column(Boolean, nullable=True, comment='Indica se o atributo é obrigatório')
    DefaultValue = Column(String, nullable=True, comment='Armazena o valor padrão do atributo')
    ValidationRules = Column(String, nullable=True, comment='Especifica regras de validação personalizadas para o atributo')
    IsIndexed = Column(Boolean, nullable=True, comment='Indica se o atributo é indexado para consultas mais rápidas')
    IsUnique = Column(Boolean, nullable=True, comment='Indica se os valores do atributo devem ser únicos')
    MinimumValue = Column(DECIMAL(18, 6), nullable=True, comment='Especifica o valor mínimo para o atributo')
    MaximumValue = Column(DECIMAL(18, 6), nullable=True, comment='Especifica o valor máximo para o atributo')
    ForeignKeyEntity = Column(Integer, nullable=True, comment='Referencia entidades relacionadas (se o atributo for uma chave estrangeira)')
    IsHidden = Column(Boolean, nullable=True, comment='Indica se o atributo deve ser oculto na interface do usuário')
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )
    