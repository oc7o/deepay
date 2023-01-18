import requests
import typing
from requests import Session
from decimal import Decimal
from octoincore.config.models import ServerSettings


class BTCPayClient:
    client: Session
    token: str
    btcpay_instance: str
    default_store_id: str
    default_currency: str

    def __init__(self) -> None:
        self.client = Session()
        self.client.headers["Content-Type"] = "application/json"
        self.client.headers["Authorization"] = "token " + self.token

    def get_stores(self):
        return self.client.get(self.btcpay_instance + "/api/v1/stores").json()

    def get_store(self, storeId: str = default_store_id):
        return self.client.get(
            self.btcpay_instance + "/api/v1/stores/" + storeId
        ).json()

    def get_invoices(self, storeId: str = default_store_id):
        return self.client.get(
            self.btcpay_instance + f"/api/v1/stores/{storeId}/invoices"
        ).json()

    def get_invoice(self, invoiceId: str, storeId: str = default_store_id):
        return self.client.get(
            self.btcpay_instance + f"/api/v1/stores/{storeId}/invoices/{invoiceId}"
        ).json()

    def create_invoice(self, amount: Decimal, storeId: str = default_store_id):
        data = {
            "checkout": {
                "speedPolicy": "HighSpeed",  # "Highspeed": 0, "MediumSpeed": 1, "LowMediumSpeed": 2, "LowSpeed": 6
                "paymentMethods": ["BTC"],
                "defaultPaymentMethod": "BTC",
                "expirationMinutes": 60 * 24,
                "monitoringMinutes": 60 * 24,
                "paymentTolerance": 100,
                "redirectURL": "https://google.com/",  # https://sloow.de/
                "redirectAutomatically": True,
                "requiresRefundEmail": False,
                "defaultLanguage": "en-US",
            },
            "receipt": {"enabled": True, "showQR": None, "showPayments": None},
            "amount": amount,
            "currency": self.default_currency,
        }
        """
        # "metadata": {
        #     "orderId": "string",
        #     "orderUrl": "string"
        # },

        # "additionalSearchTerms": [
        #     "string"
        # ]
        """
        return self.client.post(
            self.btcpay_instance + f"/api/v1/stores/{storeId}/invoices", json=data
        ).json()


def get_btcpay_client():
    client = BTCPayClient()
    client_data = ServerSettings.objects
    client.token = client_data.get("btcpay_token")
    client.btcpay_instance = client_data.get("btcpay_instance")
    client.default_store_id = client_data.get(
        "default_store_id"
    )  # "4LV39Ej2XB3zb9VTfstnyGJ1dBgGa5ndjqYoJUsEoqNq"
    client.default_currency = client_data.get("default_currency")

