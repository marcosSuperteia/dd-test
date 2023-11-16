from typing import Any, Dict, Optional, Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.customer import Customer
from app.db.schemas.customer import CustomerCreate, CustomerUpdate, CustomerBase, CustomerInDB


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: CustomerCreate) -> Customer:
        db_obj = Customer(
            CustomerName=obj_in.CustomerName,
            Description=obj_in.Description
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(self, db: AsyncSession, *, db_obj: Customer,
                     obj_in: Union[CustomerUpdate, Dict[str, Any]]) -> Customer:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)
    

customer = CRUDCustomer(Customer)