from milto.common import read_json_from_web_api
from milto.etl import COINGECKO_GET_COINS_ENDPOINT


class TestReadJsonFromWebApi:
    def test_read_json_from_web_api_200(self):
        response = read_json_from_web_api(
            api_url=COINGECKO_GET_COINS_ENDPOINT,
            headers={},
            params={
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": 100,
                "page": 1
            }
        )

        assert len(response) == 100
