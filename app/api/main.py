from fastapi import APIRouter
from app.api.routers.transactions.router import transaction_router
from app.api.routers.wallets.router import wallets_router

api_router = APIRouter()


api_router.include_router(
    transaction_router, prefix="/transactions", tags=["transactions"]
)

api_router.include_router(wallets_router, prefix="/wallets", tags=["wallets"])
