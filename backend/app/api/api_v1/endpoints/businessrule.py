from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.BusinessRule])
async def read_businessrules(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.BusinessRule = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve businessrules.
    """
    businessrules = await repositories.businessrule.get_multi(db, skip=skip, limit=limit)
    return businessrules


@router.post("/", response_model=schemas.BusinessRule)
async def create_businessrule(
    *,
    db: AsyncSession = Depends(deps.get_db),
    businessrule_in: schemas.BusinessRuleCreate,
    _: models.BusinessRule = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new businessrule.
    """
    businessrule = await repositories.businessrule.create(db, obj_in=businessrule_in)
    return businessrule


@router.put("/{id}", response_model=schemas.BusinessRule)
async def update_businessrule(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    businessrule_in: schemas.BusinessRuleUpdate,
    _: models.BusinessRule = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an businessrule.
    """
    businessrule = await repositories.businessrule.get(db, id)
    if not businessrule:
        raise HTTPException(
            status_code=404,
            detail="The businessrule with this id does not exist in the system.",
        )
    businessrule = await repositories.businessrule.update(db, db_obj=businessrule, obj_in=businessrule_in)
    return businessrule


@router.get("/{id}", response_model=schemas.BusinessRule)
async def read_businessrule_by_id(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    _: models.BusinessRule = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get businessrule by id.
    """
    businessrule = await repositories.businessrule.get(db, id)
    if not businessrule:
        raise HTTPException(
            status_code=404,
            detail="The businessrule with this id does not exist in the system.",
        )
    return businessrule


@router.delete("/{id}", response_model=schemas.BusinessRule)
async def delete_businessrule(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    _: models.BusinessRule = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an businessrule.
    """
    businessrule = await repositories.businessrule.get(db, id)
    if not businessrule:
        raise HTTPException(
            status_code=404,
            detail="The businessrule with this id does not exist in the system.",
        )
    businessrule = await repositories.businessrule.remove(db, id=id)
    return businessrule