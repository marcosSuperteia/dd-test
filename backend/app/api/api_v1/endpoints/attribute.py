from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.Attribute])
async def read_attributes(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.Attribute = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve attributes.
    """
    attributes = await repositories.attribute.get_multi(db, skip=skip, limit=limit)
    return attributes


@router.post("/", response_model=schemas.Attribute)
async def create_attribute(
    *,
    db: AsyncSession = Depends(deps.get_db),
    attribute_in: schemas.AttributeCreate,
    _: models.Attribute = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new attribute.
    """
    attribute = await repositories.attribute.create(db, obj_in=attribute_in)
    return attribute


@router.put("/{AttributeID}", response_model=schemas.Attribute)
async def update_attribute(
    *,
    db: AsyncSession = Depends(deps.get_db),
    AttributeID: int,
    attribute_in: schemas.AttributeUpdate,
    _: models.Attribute = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an attribute.
    """
    attribute = await repositories.attribute.get(db, id=AttributeID)
    if not attribute:
        raise HTTPException(
            status_code=404,
            detail="The attribute with this AttributeID does not exist in the system.",
        )
    attribute = await repositories.attribute.update(db, db_obj=attribute, obj_in=attribute_in)
    return attribute


@router.get("/{AttributeID}", response_model=schemas.Attribute)
async def read_attribute_by_AttributeID(
    *,
    db: AsyncSession = Depends(deps.get_db),
    AttributeID: int,
    _: models.Attribute = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get attribute by AttributeID.
    """
    attribute = await repositories.attribute.get(db, id=AttributeID)
    if not attribute:
        raise HTTPException(
            status_code=404, detail="The attribute with this AttributeID does not exist."
        )
    return attribute


@router.delete("/{AttributeID}", response_model=schemas.Attribute)
async def delete_attribute(
    *,
    db: AsyncSession = Depends(deps.get_db),
    AttributeID: int,
    _: models.Attribute = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an attribute.
    """
    attribute = await repositories.attribute.get(db, id=AttributeID)
    if not attribute:
        raise HTTPException(
            status_code=404,
            detail="The attribute with this AttributeID does not exist in the system.",
        )
    attribute = await repositories.attribute.remove(db, id=AttributeID)
    return attribute

