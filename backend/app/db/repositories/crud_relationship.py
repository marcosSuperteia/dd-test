from typing import Any, Dict, Optional, Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.relationship import Relationship
from app.db.schemas.relationship import RelationshipCreate, RelationshipUpdate, RelationshipBase, RelationshipInDB


class CRUDRelationship(CRUDBase[Relationship, RelationshipCreate, RelationshipUpdate]):
    async def create(self, db: AsyncSession, *, obj_in: RelationshipCreate) -> Relationship:
        db_obj = Relationship(
            ParentEntityID=obj_in.ParentEntityID,
            ChildEntityID=obj_in.ChildEntityID,
            Description=obj_in.Description
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(self, db: AsyncSession, *, db_obj: Relationship,
                     obj_in: Union[RelationshipUpdate, Dict[str, Any]]) -> Relationship:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)


relationship = CRUDRelationship(Relationship)