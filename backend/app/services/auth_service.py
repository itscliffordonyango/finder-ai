from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class AuthService:
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def register(self, user_data: UserCreate):
        existing_user = await self.user_repository.get_by_email(
            user_data.email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        return await self.user_repository.create(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=hash_password(user_data.password),
        )

    async def authenticate_user(
        self,
        email: str,
        password: str,
    ):
        user = await self.user_repository.get_by_email(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }