from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup and shutdown events.

    Resources such as the database, Redis connections,
    schedulers, or background workers can be initialized here.
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


@app.get("/", tags=["Root"])
async def root():
    return {
        "success": True,
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "success": True,
        "status": "healthy",
    }