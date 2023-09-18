from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("", status_code=200)
async def health():
    return {"status": "OK"}
