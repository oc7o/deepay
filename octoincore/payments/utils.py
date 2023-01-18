BTCPAY_HOST = ""

from btcpay import BTCPayClient

from .models import BTCPayClientStore


def get_btcpay_client() -> BTCPayClient:
    client = BTCPayClientStore.objects.first().client
    return client

def create_btcpay_client(code, host):
    client = BTCPayClient.create_client(host=host, code=code)
    BTCPayClientStore.objects.create(client=client)
