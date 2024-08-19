from fastapi import APIRouter, Response, status
from app.errors import NotFoundError
from app.external_api.GoldRush import goldRush_api

wallets_router = APIRouter()


@wallets_router.get("/{wallet_address}/chains/{chain_name}/assets", status_code=200)
async def wallet_assets_by_chain(
    wallet_address: str, chain_name: str, response: Response
):
    try:
        return goldRush_api.wallet_assets_by_chain(
            walletAddress=wallet_address, chainName=chain_name
        )["data"]["items"]

    except NotFoundError:
        response.status_code = status.HTTP_404_NOT_FOUND


@wallets_router.get("/{wallet_address}/chains/{chain_name}/value", status_code=200)
async def wallet_assets_by_chain(
    wallet_address: str, chain_name: str, response: Response
):
    try:
        sum = 0

        for asset in goldRush_api.wallet_assets_by_chain(
            walletAddress=wallet_address, chainName=chain_name
        )["data"]["items"]:
            quote = asset["quote_rate"]

            if quote is not None:
                sum = sum + quote

        return sum
    except NotFoundError:
        response.status_code = status.HTTP_404_NOT_FOUND


@wallets_router.get(
    "/{wallet_address}/chains/{chain_name}/transactions/", status_code=200
)
async def wallet_assets_by_chain(
    wallet_address: str,
    chain_name: str,
    page: int,
    response: Response,
):
    try:
        return goldRush_api.wallet_transactions_by_chain(
            walletAddress=wallet_address, chainName=chain_name, page=page
        )["data"]["items"]

    except NotFoundError:
        response.status_code = status.HTTP_404_NOT_FOUND
