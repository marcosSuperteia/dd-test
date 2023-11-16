from typing import Any, Dict, Optional, Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.businessrule import BusinessRule
from app.db.schemas.businessrule import BusinessRuleCreate, BusinessRuleUpdate, BusinessRuleBase, BusinessRuleInDB


class CRUDBusinessRule(CRUDBase[BusinessRule, BusinessRuleCreate, BusinessRuleUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: BusinessRuleCreate) -> BusinessRule:
        db_obj = BusinessRule(
            EntityID=obj_in.EntityID,
            RuleName=obj_in.RuleName,
            RuleDescription=obj_in.RuleDescription,
            SystemID=obj_in.SystemID
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(self, db: AsyncSession, *, db_obj: BusinessRule,
                     obj_in: Union[BusinessRuleUpdate, Dict[str, Any]]) -> BusinessRule:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)
    

businessrule = CRUDBusinessRule(BusinessRule)