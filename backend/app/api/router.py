from fastapi import APIRouter

api_router = APIRouter()

# Future routers
# from app.api.v1.auth import router as auth_router
# api_router.include_router(
#     auth_router,
#     prefix="/auth",
#     tags=["Authentication"],
# )