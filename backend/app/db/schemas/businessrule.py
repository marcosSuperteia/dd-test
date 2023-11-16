from typing import List, Optional # noqa: F401, E261
# from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr


class BusinessRuleBase(BaseModel):
    EntityID: Optional[int] = None
    RuleName: Optional[str] = None
    RuleDescription: Optional[str] = None
    SystemID: Optional[int] = None


class BusinessRuleCreate(BusinessRuleBase):
    EntityID: int
    RuleName: str
    RuleDescription: str
    SystemID: int


class BusinessRuleUpdate(BusinessRuleBase):
    EntityID: Optional[int] = None
    RuleName: Optional[str] = None
    RuleDescription: Optional[str] = None
    SystemID: Optional[int] = None


class BusinessRuleInDBBase(BusinessRuleBase):
    id: int
    class Config:
        orm_mode = True


class BusinessRule(BusinessRuleInDBBase):
    pass


class BusinessRuleInDB(BusinessRuleInDBBase):
    pass


