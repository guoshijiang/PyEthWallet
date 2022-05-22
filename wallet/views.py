# encoding=utf-8
from django.shortcuts import redirect, render
from wallet.address import create_address
from wallet.rpc import RpcClient
from wallet.tx import Transaction
from common.helpers import dec


RpcUrl = "https://eth-ropsten.alchemyapi.io/v2/KE3V4NLUN3fgvie0lbTHyQ8Q2zSSnfo2"


def create_addr(request):
    address = create_address()
    privkey = address.get("privkey")
    public_key = address.get("public_key")
    eth_address = address.get("address")
    return render(request, "front/index.html", locals())


def get_balance(request):
    asset = request.GET.get("asset", "ETH")
    address = "0x26bb2fe53a40f23ec34fd15095d98a342a4d58d5"
    rc = RpcClient(RpcUrl)
    if asset == "ETH":
        balance = rc.getBalance(address, "ether")
    else:
        balance = rc.getBalance(address, "tether")
    return render(request, "front/index.html", locals())


def transfer(request):
    rc = RpcClient(RpcUrl)
    nonce = rc.getTxCount("0x26bb2fe53a40f23ec34fd15095d98a342a4d58d5")
    tx = Transaction(
        to="0xECF09D36f07EC396f97DD448D9E4bcb19fE4Ec3A",
        value=dec(1),
        gas=2000000,
        maxFeePerGas=2000000000,
        maxPriorityFeePerGas=1000000000,
        nonce=nonce,
        chainId=3
    )
    priv = "59488f5fd5489d7166f6563e30fc6fcd39e08e1f3f0ccec13beba56a35920371"
    signMsg = tx.signTx(tx.buildTx("0x00"), priv)
    txHash = rc.sendTx(signMsg)
    return render(request, "front/index.html", locals())





