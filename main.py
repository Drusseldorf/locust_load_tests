from http_requests.get_status import get_status
from http_requests.pay_orders import make_order
from http_requests.send_sms import send_sms
from locust import HttpUser, task
import gevent


class ToSuccessViaSmsReader(HttpUser):

    @task
    def success_via_sms(self):
        payin_response = make_order.payin(http_client=self)

        gevent.sleep(1)

        get_status_response = get_status(
            http_client=self, order_id=payin_response.json()["id"]
        )

        send_sms(
            http_client=self,
            card=get_status_response.json()["card"]["number"],
            amount=get_status_response.json()["to_be_paid"],
        )
