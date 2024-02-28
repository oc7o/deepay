from django.conf import settings
from .btcpayserver_client import BTCPayClient


def get_btcpay_client():
    print(settings.BTCPAY_SERVER_URL)
    client = BTCPayClient(
        token=settings.BTCPAY_TOKEN,
        btcpay_instance=settings.BTCPAY_SERVER_URL,
        default_store_id=settings.BTCPAY_STORE_ID,
        default_currency=settings.BTCPAY_CURRENCY,
    )  # "EUR"
    return client


# def create_btcpay_client(code, host):
#     client = BTCPayClient.create_client(host=host, code=code)
#     BTCPayClientStore.objects.create(client=client)
