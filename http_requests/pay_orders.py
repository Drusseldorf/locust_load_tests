from requests import Response
from locust import HttpUser
from config import settings
from utils.get_payload import get_payload_for


class MakeOrder:

    HEADERS = {
        "SECRET-TOKEN": settings.company.token,
        "Content-Type": "application/json",
    }
    PAYIN_ENDPOINT = "/api/v1/h2h/payments"
    PAYOUT_ENDPOINT = "/api/v1/payouts"

    def payout(self, http_client: HttpUser) -> Response:

        payload = get_payload_for.payout()
        response = http_client.client.post(
            url=self.PAYOUT_ENDPOINT, headers=self.HEADERS, json=payload
        )

        return response

    def payin(self, http_client: HttpUser) -> Response:

        payload = get_payload_for.payin()

        response = http_client.client.post(
            url=self.PAYIN_ENDPOINT, headers=self.HEADERS, json=payload
        )

        return response


make_order = MakeOrder()
