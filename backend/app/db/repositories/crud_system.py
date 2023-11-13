from typing import Any, Dict, Optional, Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.system import System
from app.db.schemas.system import SystemCreate, SystemUpdate, SystemBase, SystemInDB


class CRUDSystem(CRUDBase[System, SystemCreate, SystemUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: SystemCreate) -> System:
        db_obj = System(
            SystemName=obj_in.SystemName,
            SystemPrefix=obj_in.SystemPrefix,
            Description=obj_in.Description,
            CustomerID=obj_in.CustomerID,
            data_entry_order=obj_in.data_entry_order
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(self, db: AsyncSession, *, db_obj: System,
                     obj_in: Union[SystemUpdate, Dict[str, Any]]) -> System:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)
    

system = CRUDSystem(System)