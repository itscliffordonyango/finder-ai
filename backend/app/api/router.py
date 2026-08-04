from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.resume import router as resume_router

from app.api.v1.jobs import router as jobs_router
from app.api.v1.match import router as match_router
from app.api.v1.analysis import router as analysis_router
from app.api.v1.ats import router as ats_router



api_router = APIRouter()

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"],
)

api_router.include_router(
    resume_router,
    prefix="/resumes",
    tags=["Resumes"],
)

api_router.include_router(
    jobs_router,
    prefix="/jobs",
    tags=["Jobs"],
)

api_router.include_router(
    match_router,
    prefix="/match",
    tags=["AI Matching"],
)

api_router.include_router(
    analysis_router,
    prefix="/analysis",
    tags=["AI Analysis"],
)

api_router.include_router(
    ats_router,
    prefix="/ats",
    tags=["ATS Analysis"],
)