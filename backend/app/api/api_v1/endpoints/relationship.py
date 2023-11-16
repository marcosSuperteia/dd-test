from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.Relationship])
async def read_relationships(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.Relationship = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve relationships.
    """
    relationships = await repositories.relationship.get_multi(db, skip=skip, limit=limit)
    return relationships


@router.post("/", response_model=schemas.Relationship)
async def create_relationship(
    *,
    db: AsyncSession = Depends(deps.get_db),
    relationship_in: schemas.RelationshipCreate,
    _: models.Relationship = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new relationship.
    """
    relationship = await repositories.relationship.create(db, obj_in=relationship_in)
    return relationship


@router.put("/{id}", response_model=schemas.Relationship)
async def update_relationship(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    relationship_in: schemas.RelationshipUpdate,
    _: models.Relationship = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an relationship.
    """
    relationship = await repositories.relationship.get(db, id)
    if not relationship:
        raise HTTPException(
            status_code=404,
            detail="The relationship with this id does not exist in the system.",
        )
    relationship = await repositories.relationship.update(db, db_obj=relationship, obj_in=relationship_in)
    return relationship


@router.get("/{id}", response_model=schemas.Relationship)
async def read_relationship_by_id(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    _: models.Relationship = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get relationship by id.
    """
    relationship = await repositories.relationship.get(db, id)
    if not relationship:
        raise HTTPException(
            status_code=404,
            detail="The relationship with this id does not exist in the system.",
        )
    return relationship



@router.delete("/{id}", response_model=schemas.Relationship)
async def delete_relationship(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    _: models.Relationship = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an relationship.
    """
    relationship = await repositories.relationship.get(db, id)
    if not relationship:
        raise HTTPException(
            status_code=404,
            detail="The relationship with this id does not exist in the system.",
        )
    relationship = await repositories.relationship.remove(db, id=id)
    return relationship
