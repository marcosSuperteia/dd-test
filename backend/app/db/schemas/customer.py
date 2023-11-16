from typing import List, Optional # noqa: F401, E261
# from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr


class CustomerBase(BaseModel):
    CustomerName: Optional[str] = None
    Description: Optional[str] = None
    


class CustomerCreate(CustomerBase):
    CustomerName: str
    Description: str


class CustomerUpdate(CustomerBase):
    CustomerName: Optional[str] = None
    Description: Optional[str] = None


class CustomerInDBBase(CustomerBase):
    id: int
    class Config:
        orm_mode = True


class Customer(CustomerInDBBase):
    pass


class CustomerInDB(CustomerInDBBase):
    pass