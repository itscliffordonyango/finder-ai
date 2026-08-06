from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.services.dashboard_service import DashboardService

router = APIRouter()


@router.get("/")
async def dashboard(
    db: AsyncSession = Depends(get_db),
):
    service = DashboardService(db)
    return await service.get_dashboard()