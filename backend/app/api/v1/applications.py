from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.application import (
    ApplicationResponse,
    UpdateStatusRequest,
)
from app.services.application_service import (
    ApplicationService,
)

router = APIRouter()

@router.post(
    "/save/{user_id}/{job_id}",
    response_model=ApplicationResponse,
)
async def save_job(
    user_id: int,
    job_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = ApplicationService(db)

    return await service.save_job(
        user_id,
        job_id,
    )

@router.get(
    "/{user_id}",
    response_model=list[ApplicationResponse],
)
async def list_saved_jobs(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = ApplicationService(db)

    return await service.list_saved(
        user_id,
    )

@router.patch(
    "/{user_id}/{job_id}",
    response_model=ApplicationResponse,
)
async def update_status(
    user_id: int,
    job_id: int,
    request: UpdateStatusRequest,
    db: AsyncSession = Depends(get_db),
):
    service = ApplicationService(db)

    application = await service.update_status(
        user_id,
        job_id,
        request.status,
    )

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found",
        )

    return application

@router.delete(
    "/{user_id}/{job_id}",
)
async def remove_saved_job(
    user_id: int,
    job_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = ApplicationService(db)

    deleted = await service.remove_saved_job(
        user_id,
        job_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Application not found",
        )

    return {
        "message": "Job removed successfully"
    }