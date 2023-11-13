from typing import List, Optional
from pydantic import BaseModel



class EntityBase(BaseModel):
    EntityName: Optional[str] = None
    Description: Optional[str] = None
    SystemID: Optional[int] = None


class EntityCreate(EntityBase):
    EntityName: str
    Description: str
    SystemID: int


class EntityUpdate(EntityBase):
    EntityName: Optional[str] = None
    Description: Optional[str] = None
    SystemID: Optional[int] = None


class EntityInDBBase(EntityBase):
    id: int

    class Config:
        orm_mode = True


class Entity(EntityInDBBase):
    pass


class EntityInDB(EntityInDBBase):
    pass
