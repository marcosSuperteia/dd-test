from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users # noqa: E501, E261
from app.api.api_v1.endpoints import system # noqa: E501, E261

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(system.router, prefix="/systems", tags=["systems"])