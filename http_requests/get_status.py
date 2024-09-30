from requests import Response
from locust import HttpUser
from config import settings


def get_status(order_id: str, http_client: HttpUser) -> Response:

    ENDPOINT = f"/api/v1/h2h/payments/{order_id}"
    HEADERS = {"SECRET-TOKEN": settings.company.token}

    response = http_client.client.get(url=ENDPOINT, headers=HEADERS, name="get_status")

    return response
