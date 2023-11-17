from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.UIElement])
async def read_uielements(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.UIElement = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve uielements.
    """
    uielements = await repositories.uielement.get_multi(db, skip=skip, limit=limit)
    return uielements


@router.post("/", response_model=schemas.UIElement)
async def create_uielement(
    *,
    db: AsyncSession = Depends(deps.get_db),
    uielement_in: schemas.UIElementCreate,
    _: models.UIElement = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new uielement.
    """
    uielement = await repositories.uielement.create(db, obj_in=uielement_in)
    return uielement


@router.put("/{id}", response_model=schemas.UIElement)
async def update_uielement(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    uielement_in: schemas.UIElementUpdate,
    _: models.UIElement = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an uielement.
    """
    uielement = await repositories.uielement.get(db, id)
    if not uielement:
        raise HTTPException(
            status_code=404,
            detail="The uielement with this id does not exist in the system.",
        )
    uielement = await repositories.uielement.update(db, db_obj=uielement, obj_in=uielement_in)
    return uielement


@router.get("/{id}", response_model=schemas.UIElement)
async def read_uielement_by_id(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    _: models.UIElement = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get uielement by id.
    """
    uielement = await repositories.uielement.get(db, id)
    if not uielement:
        raise HTTPException(
            status_code=404,
            detail="The uielement with this id does not exist in the system.",
        )
    return uielement


@router.delete("/{id}", response_model=schemas.UIElement)
async def delete_uielement(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    _: models.UIElement = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an uielement.
    """
    uielement = await repositories.uielement.get(db, id)
    if not uielement:
        raise HTTPException(
            status_code=404,
            detail="The uielement with this id does not exist in the system.",
        )
    uielement = await repositories.uielement.remove(db, id=id)
    return uielement