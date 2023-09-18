from app.waypoint.services import WaypointService
from fastapi import APIRouter

waypoint_router = APIRouter()


@waypoint_router.get("/{airport}/sid/top")
async def waypoint_top_sid(airport):
    return WaypointService().get_top_waypoints_sid(airport)


@waypoint_router.get("/{airport}/star/top")
async def waypoint_top_star(airport):
    return WaypointService().get_top_waypoints_star(airport)
