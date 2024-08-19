from httpx import Client
from app.config import settings
from app.errors import NotFoundError


class GoldRushWrapper:
    url: str = "https://api.covalenthq.com/v1"
    client: Client

    def __init__(self) -> None:
        self.client = Client(base_url=self.url)

    def wallet_assets_by_chain(self, chainName: str, walletAddress: str):
        response = self.client.get(
            f"/{chainName}/address/{walletAddress}/balances_v2/",
            params={"key": settings.GOLDRUSH_API_KEY, "quote-currency": "USD"},
        )
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise NotFoundError()
        else:
            raise RuntimeError(response)


goldRush_api = GoldRushWrapper()
