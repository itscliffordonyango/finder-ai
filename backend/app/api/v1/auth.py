from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService

from app.schemas.auth import LoginRequest
from app.schemas.token import Token

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(db)

    return await service.register(user)

@router.post(
    "/login",
    response_model=Token,
)
async def login(
    credentials: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(db)

    return await service.authenticate_user(
        credentials.email,
        credentials.password,
    )