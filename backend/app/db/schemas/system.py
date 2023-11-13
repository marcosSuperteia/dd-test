from typing import List, Optional # noqa: F401, E261
# from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr


class SystemBase(BaseModel):
    SystemName: Optional[str] = None
    SystemPrefix: Optional[str] = None
    Description: Optional[str] = None
    CustomerID: Optional[int] = None
    data_entry_order: Optional[str] = None


class SystemCreate(SystemBase):
    SystemName: str
    SystemPrefix: str
    Description: str
    CustomerID: int
    data_entry_order: str


class SystemUpdate(SystemBase):
    SystemName: Optional[str] = None
    SystemPrefix: Optional[str] = None
    Description: Optional[str] = None
    CustomerID: Optional[int] = None
    data_entry_order: Optional[str] = None


class SystemInDBBase(SystemBase):
    id: int
    class Config:
        orm_mode = True


class System(SystemInDBBase):
    pass


class SystemInDB(SystemInDBBase):
    pass


