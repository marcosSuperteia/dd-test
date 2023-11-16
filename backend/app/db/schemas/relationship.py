from typing import List, Optional # noqa: F401, E261
# from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr


class RelationshipBase(BaseModel):
    ParentEntityID: Optional[int] = None
    ChildEntityID: Optional[int] = None
    Description: Optional[str] = None


class RelationshipCreate(RelationshipBase):
    ParentEntityID: int
    ChildEntityID: int
    Description: str


class RelationshipUpdate(RelationshipBase):
    ParentEntityID: Optional[int] = None
    ChildEntityID: Optional[int] = None
    Description: Optional[str] = None


class RelationshipInDBBase(RelationshipBase):
    id: int
    class Config:
        orm_mode = True


class Relationship(RelationshipInDBBase):
    pass


class RelationshipInDB(RelationshipInDBBase):
    pass
