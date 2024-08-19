from httpx import Client, Auth
from app.config import settings


class GoldRushAuth(Auth):
    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
        # Send the request, with a custom `X-Authentication` header.
        request.headers["API_KEY"] = self.token
        yield request


class GoldRushWrapper:
    url: str = "https://api.covalenthq.com/v1"
    client: Client

    def __init__(self) -> None:
        auth = GoldRushAuth(settings.GOLDRUSH_API_KEY)
        self.client = Client(base_url=self.url, auth=auth)

    def wallet_assets_by_chain(self, chainName: str, walletAddress: str):
        response = self.client.get(
            f"/v1/{chainName}/address/{walletAddress}/balances_v2/"
        )
        return response.json()


goldRush_api = GoldRushWrapper()
