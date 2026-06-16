from fastapi import APIRouter
from src.account.router import router as account_router

router = APIRouter(
    prefix="/api",
)

router.include_router(account_router)
