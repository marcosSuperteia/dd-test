from typing import Any, Dict, Optional, Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.entity import Entity
from app.db.schemas.entity import EntityCreate, EntityUpdate, EntityBase, EntityInDB


class CRUDEntity(CRUDBase[Entity, EntityCreate, EntityUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: EntityCreate) -> Entity:
        db_obj = Entity(
            EntityName=obj_in.EntityName,
            Description=obj_in.Description,
            SystemID=obj_in.SystemID
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(self, db: AsyncSession, *, db_obj: Entity,
                     obj_in: Union[EntityUpdate, Dict[str, Any]]) -> Entity:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)
    

entity = CRUDEntity(Entity)