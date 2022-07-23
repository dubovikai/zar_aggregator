from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, utils
from app.api.api_v1.endpoints import attractions, organizations, events

api_router = APIRouter()
api_router.include_router(login.router, 
                            tags=["login"])
api_router.include_router(users.router, 
                            prefix="/users", tags=["users"])
api_router.include_router(utils.router, 
                            prefix="/utils", tags=["utils"])
api_router.include_router(attractions.router, 
                            prefix="/attractions", tags=["attraction"])
api_router.include_router(organizations.router, 
                            prefix="/organizations", tags=["organization"])
api_router.include_router(events.router, 
                            prefix="/events", tags=["event"])
