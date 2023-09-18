from fastapi import APIRouter

from api.waypoint import waypoint_router
from api.health import health_router

router = APIRouter()
router.include_router(health_router, prefix="/health")
router.include_router(waypoint_router, prefix="/api/waypoint")


__all__ = ["router"]
