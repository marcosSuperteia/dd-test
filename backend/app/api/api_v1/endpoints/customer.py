from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.Customer])
async def read_customers(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.Customer = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve customers.
    """
    customers = await repositories.customer.get_multi(db, skip=skip, limit=limit)
    return customers


@router.post("/", response_model=schemas.Customer)
async def create_customer(
    *,
    db: AsyncSession = Depends(deps.get_db),
    customer_in: schemas.CustomerCreate,
    _: models.Customer = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new customer.
    """
    customer = await repositories.customer.create(db, obj_in=customer_in)
    return customer


@router.put("/{id}", response_model=schemas.Customer)
async def update_customer(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    customer_in: schemas.CustomerUpdate,
    _: models.Customer = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an customer.
    """
    customer = await repositories.customer.get(db, id)
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="The customer with this id does not exist in the system.",
        )
    customer = await repositories.customer.update(db, db_obj=customer, obj_in=customer_in)
    return customer



@router.get("/{id}", response_model=schemas.Customer)
async def read_customer_by_id(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    _: models.Customer = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get customer by id.
    """
    customer = await repositories.customer.get(db, id=id)
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="The customer with this id does not exist in the system.",
        )
    return customer



@router.delete("/{id}", response_model=schemas.Customer)
async def delete_customer(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    _: models.Customer = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an customer.
    """
    customer = await repositories.customer.get(db, id=id)
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="The customer with this id does not exist in the system.",
        )
    customer = await repositories.customer.remove(db, id=id)
    return customer
