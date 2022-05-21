import json
from web3 import Web3
from decimal import Decimal


EIP20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501


class Transaction:
    to: str
    value: Decimal
    gas: int
    maxFeePerGas: int
    maxPriorityFeePerGas: int
    nonce: int
    chainId: int

    def __init__(
        self,
        to: str,
        value: Decimal,
        gas: int,
        maxFeePerGas: int,
        maxPriorityFeePerGas: int,
        nonce: int,
        chainId: int
    ):
        self.to = to
        self.value = value
        self.gas = gas
        self.maxFeePerGas = maxFeePerGas
        self.maxPriorityFeePerGas = maxPriorityFeePerGas
        self.nonce = nonce
        self.chainId = chainId

    def buildTx(self, contractAddress):
        if contractAddress != "0x00":
            contractCoin = Web3.eth.contract(address=contractAddress, abi=EIP20_ABI)
            unsignTx = contractCoin.functions.transfer(
                self.to,
                Web3.toWei(self.value, "18"),
            ).buildTransaction({
                'chainId': self.chainId,
                'gas': self.gas,
                'maxFeePerGas':self.maxFeePerGas,
                'maxPriorityFeePerGas': self.maxPriorityFeePerGas,
                'nonce': self.nonce
           })
        else:
            unsignTx = {
                'to': self.to,
                'value': Web3.toWei(self.value, "18"),
                'gas': self.gas,
                'maxFeePerGas': self.maxFeePerGas,
                'maxPriorityFeePerGas': self.maxPriorityFeePerGas,
                'nonce': self.nonce,
                'chainId': self.chainId
            }
        return unsignTx

    def signTx(self, tx, priv):
        Web3.eth.signTransaction(tx, priv)

