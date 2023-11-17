from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users # noqa: E501, E261
from app.api.api_v1.endpoints import system # noqa: E501, E261
from app.api.api_v1.endpoints import entity # noqa: E501, E261
from app.api.api_v1.endpoints import attribute # noqa: E501, E261
from app.api.api_v1.endpoints import businessrule # noqa: E501, E261
from app.api.api_v1.endpoints import customer # noqa: E501, E261
from app.api.api_v1.endpoints import relationship # noqa: E501, E261
from app.api.api_v1.endpoints import uielement # noqa: E501, E261

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(system.router, prefix="/systems", tags=["systems"])
api_router.include_router(entity.router, prefix="/entities", tags=["entities"])
api_router.include_router(attribute.router, prefix="/attributes", tags=["attributes"])
api_router.include_router(businessrule.router, prefix="/businessrules", tags=["businessrules"])
api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
api_router.include_router(relationship.router, prefix="/relationships", tags=["relationships"])
api_router.include_router(uielement.router, prefix="/uielements", tags=["uielements"])