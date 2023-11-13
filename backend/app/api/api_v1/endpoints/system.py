from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.System])
async def read_systems(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.System = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve systems.
    """
    systems = await repositories.system.get_multi(db, skip=skip, limit=limit)
    return systems


@router.post("/", response_model=schemas.System)
async def create_system(
    *,
    db: AsyncSession = Depends(deps.get_db),
    system_in: schemas.SystemCreate,
    _: models.System = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new system.
    """
    system = await repositories.system.create(db, obj_in=system_in)
    return system


@router.put("/{SystemID}", response_model=schemas.System)
async def update_system(
    *,
    db: AsyncSession = Depends(deps.get_db),
    SystemID: int,
    system_in: schemas.SystemUpdate,
    _: models.System = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an system.
    """
    system = await repositories.system.get(db, SystemID)
    if not system:
        raise HTTPException(
            status_code=404,
            detail="The system with this SystemID does not exist in the system.",
        )
    system = await repositories.system.update(db, db_obj=system, obj_in=system_in)
    return system


@router.get("/{SystemID}", response_model=schemas.System)
async def read_system_by_SystemID(
    SystemID: int,
    db: AsyncSession = Depends(deps.get_db),
    _: models.System = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get system by SystemID.
    """
    system = await repositories.system.get(db, SystemID)
    if not system:
        raise HTTPException(
            status_code=404,
            detail="The system with this SystemID does not exist in the system.",
        )
    return system


@router.delete("/{SystemID}", response_model=schemas.System)
async def delete_system(
    *,
    db: AsyncSession = Depends(deps.get_db),
    SystemID: int,
    _: models.System = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an system.
    """
    system = await repositories.system.get(db, SystemID)
    if not system:
        raise HTTPException(
            status_code=404,
            detail="The system with this SystemID does not exist in the system.",
        )
    system = await repositories.system.remove(db, id=SystemID)
    return system