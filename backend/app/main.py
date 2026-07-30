from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan events.
    """

    print(f"Starting {settings.APP_NAME}...")

    yield

    print(f"Stopping {settings.APP_NAME}...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered Job Discovery Platform",
    lifespan=lifespan,
)

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {
        "success": True,
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


# Health endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "success": True,
        "status": "healthy",
    }


# Register API routes
app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX,
)