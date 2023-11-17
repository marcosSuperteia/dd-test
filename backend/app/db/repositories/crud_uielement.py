from typing import Any, Dict, Optional, Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.uielement import UIElement
from app.db.schemas.uielement import UIElementCreate, UIElementUpdate, UIElementBase, UIElementInDB


class CRUDUIElement(CRUDBase[UIElement, UIElementCreate, UIElementUpdate]):
    async def create(self, db: AsyncSession, *, obj_in: UIElementCreate) -> UIElement:
        db_obj = UIElement(
            EntityID=obj_in.EntityID,
            ElementType=obj_in.ElementType,
            ElementName=obj_in.ElementName,
            ElementDescription=obj_in.ElementDescription,
            TypingMask=obj_in.TypingMask,
            ValidationRules=obj_in.ValidationRules,
            SystemID=obj_in.SystemID
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(self, db: AsyncSession, *, db_obj: UIElement,
                     obj_in: Union[UIElementUpdate, Dict[str, Any]]) -> UIElement:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)
    

uielement = CRUDUIElement(UIElement)