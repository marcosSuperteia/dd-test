from typing import Any, Dict, Optional, Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.attribute import Attribute
from app.db.schemas.attribute import AttributeCreate, AttributeUpdate, AttributeBase, AttributeInDB


class CRUDAttribute(CRUDBase[Attribute, AttributeCreate, AttributeUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: AttributeCreate) -> Attribute:
        db_obj = Attribute(
            EntityID=obj_in.EntityID,
            AttributeName=obj_in.AttributeName,
            DataType=obj_in.DataType,
            size=obj_in.size,
            label=obj_in.label,
            tooltip=obj_in.tooltip,
            help=obj_in.help,
            IsRequired=obj_in.IsRequired,
            DefaultValue=obj_in.DefaultValue,
            ValidationRules=obj_in.ValidationRules,
            IsIndexed=obj_in.IsIndexed,
            IsUnique=obj_in.IsUnique,
            MinimumValue=obj_in.MinimumValue,
            MaximumValue=obj_in.MaximumValue,
            ForeignKeyEntity=obj_in.ForeignKeyEntity,
            IsHidden=obj_in.IsHidden
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(self, db: AsyncSession, *, db_obj: Attribute,
                     obj_in: Union[AttributeUpdate, Dict[str, Any]]) -> Attribute:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)
    

attribute = CRUDAttribute(Attribute)