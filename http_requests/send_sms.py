from locust import HttpUser
from requests import Response
from config import settings


def send_sms(card: str, amount: int, http_client: HttpUser) -> Response:

    ENDPOINT = "/api/webhooks/macrodroid_sms"
    PAYLOAD = {
        "id": settings.smsreader.id,
        "sender": settings.smsreader.sender,
        "device_id": settings.smsreader.device_id,
        "text": settings.smsreader.text.format(int(amount / 100), card[-4:]),
        "operator_token": settings.smsreader.operator_token,
        "requisite": card,
    }
    HEADERS = {"Content-Type": "application/json"}

    response = http_client.client.post(url=ENDPOINT, headers=HEADERS, json=PAYLOAD)

    return response
