from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
def pong(settings: Settings = Depends(get_settings)):  # Dependency injection
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
