from decimal import Decimal
from enum import Enum
from typing import List, Optional  # noqa: F401, E261
# from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr
from enum import Enum
from typing import List


class AttributeBase(BaseModel):
    class DataTypeEnum(str, Enum):
        Integer = 'Integer'
        Float = 'Float'
        String = 'String'
        Date = 'Date'
        Time = 'Time'
        DateTime = 'DateTime'
        Boolean = 'Boolean'
        Currency = 'Currency'
        Email = 'Email'
        URL = 'URL'
        PhoneNumber = 'Phone Number'
        Address = 'Address'
        Image = 'Image'
        File = 'File'
        Password = 'Password'

    EntityID: Optional[int]
    AttributeName: str
    DataType: Optional[DataTypeEnum]
    size: Optional[Decimal] = 0
    label: Optional[str]
    tooltip: Optional[str]
    help: Optional[str]
    IsRequired: Optional[bool]
    DefaultValue: Optional[str]
    ValidationRules: Optional[str]
    IsIndexed: Optional[bool]
    IsUnique: Optional[bool]
    MinimumValue: Optional[Decimal]
    MaximumValue: Optional[Decimal]
    ForeignKeyEntity: Optional[int]
    IsHidden: Optional[bool]





class AttributeCreate(AttributeBase):
    class DataTypeEnum(str, Enum):
        Integer = 'Integer'
        Float = 'Float'
        String = 'String'
        Date = 'Date'
        Time = 'Time'
        DateTime = 'DateTime'
        Boolean = 'Boolean'
        Currency = 'Currency'
        Email = 'Email'
        URL = 'URL'
        PhoneNumber = 'Phone Number'
        Address = 'Address'
        Image = 'Image'
        File = 'File'
        Password = 'Password'


    EntityID: int
    AttributeName: str
    DataType: Optional[DataTypeEnum]
    size: Decimal = 0
    label: str
    tooltip: str
    help: str
    IsRequired: bool
    DefaultValue: str
    ValidationRules: str
    IsIndexed: bool
    IsUnique: bool
    MinimumValue: Decimal
    MaximumValue: Decimal
    ForeignKeyEntity: int
    IsHidden: bool


class AttributeUpdate(AttributeBase):
    class DataTypeEnum(str, Enum):
        Integer = 'Integer'
        Float = 'Float'
        String = 'String'
        Date = 'Date'
        Time = 'Time'
        DateTime = 'DateTime'
        Boolean = 'Boolean'
        Currency = 'Currency'
        Email = 'Email'
        URL = 'URL'
        PhoneNumber = 'Phone Number'
        Address = 'Address'
        Image = 'Image'
        File = 'File'
        Password = 'Password'


    EntityID: Optional[int]
    AttributeName: Optional[str]
    DataType: Optional[DataTypeEnum]
    size: Optional[Decimal] = 0
    label: Optional[str]
    tooltip: Optional[str]
    help: Optional[str]
    IsRequired: Optional[bool]
    DefaultValue: Optional[str]
    ValidationRules: Optional[str]
    IsIndexed: Optional[bool]
    IsUnique: Optional[bool]
    MinimumValue: Optional[Decimal]
    MaximumValue: Optional[Decimal]
    ForeignKeyEntity: Optional[int]
    IsHidden: Optional[bool]


class AttributeInDBBase(AttributeBase):
    id: int

    class Config:
        orm_mode = True


class Attribute(AttributeInDBBase):
    pass


class AttributeInDB(AttributeInDBBase):
    pass
