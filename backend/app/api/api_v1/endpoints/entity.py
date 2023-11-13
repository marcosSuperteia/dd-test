from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.Entity])
async def read_entities(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.Entity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve entities.
    """
    entities = await repositories.entity.get_multi(db, skip=skip, limit=limit)
    return entities


@router.post("/", response_model=schemas.Entity)
async def create_entity(
    *,
    db: AsyncSession = Depends(deps.get_db),
    entity_in: schemas.EntityCreate,
    _: models.Entity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new entity.
    """
    entity = await repositories.entity.create(db, obj_in=entity_in)
    return entity


@router.put("/{EntityID}", response_model=schemas.Entity)
async def update_entity(
    *,
    db: AsyncSession = Depends(deps.get_db),
    EntityID: int,
    entity_in: schemas.EntityUpdate,
    _: models.Entity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an entity.
    """
    entity = await repositories.entity.get(db, EntityID)
    if not entity:
        raise HTTPException(
            status_code=404,
            detail="The entity with this EntityID does not exist in the system.",
        )
    entity = await repositories.entity.update(db, db_obj=entity, obj_in=entity_in)
    return entity


@router.get("/{EntityID}", response_model=schemas.Entity)
async def read_entity_by_EntityID(
    *,
    db: AsyncSession = Depends(deps.get_db),
    EntityID: int,
    _: models.Entity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get entity by EntityID.
    """
    entity = await repositories.entity.get(db, EntityID)
    if not entity:
        raise HTTPException(
            status_code=404, detail="The entity with this EntityID does not exist."
        )
    return entity


@router.delete("/{EntityID}", response_model=schemas.Entity)
async def delete_entity(
    *,
    db: AsyncSession = Depends(deps.get_db),
    EntityID: int,
    _: models.Entity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an entity.
    """
    entity = await repositories.entity.get(db, EntityID)
    if not entity:
        raise HTTPException(
            status_code=404,
            detail="The entity with this EntityID does not exist in the system.",
        )
    entity = await repositories.entity.remove(db, id=EntityID)
    return entity