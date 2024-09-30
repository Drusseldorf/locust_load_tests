import uuid
import random
from config import settings
from utils.sign_payload import sign_payload_dict


class GetPayloadFor:

    def payin(self) -> dict:
        random_amount_3000_10000 = self._random_amount_3000_10000()

        unsigned_payload = {
            "company_id": settings.company.id,
            "external_id": self._get_uuid(),
            "order_number": "LOCUST_LOAD_TEST",
            "amount": random_amount_3000_10000,
            "fail_url": "https://google.com/fail_url",
            "success_url": "https://google.com?success",
            "callback_url": "https://google.com",
            "currency": settings.payin.currency,
            "client_id": str(random_amount_3000_10000),
            "direct_method": settings.payin.direct_method,
        }

        return sign_payload_dict(unsigned_payload)

    def payout(self) -> dict:
        random_amount_3000_10000 = self._random_amount_3000_10000()

        unsigned_payload = {
            "company_id": settings.company.id,
            "external_id": self._get_uuid(),
            "order_number": "LOCUST_LOAD_TEST",
            "amount": random_amount_3000_10000,
            "fail_url": "https://google.com/fail_url",
            "success_url": "https://google.com?success",
            "callback_url": "https://google.com",
            "currency": settings.payin.currency,
            "direct_method": settings.payin.direct_method,
            "bank_name": settings.payout.bank_name,
            "customer_requisite": settings.payout.customer_requisite,
        }

        return sign_payload_dict(unsigned_payload)

    @staticmethod
    def _get_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def _random_amount_3000_10000():
        return random.randint(3000, 10000) * 100


get_payload_for = GetPayloadFor()
