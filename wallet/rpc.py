from web3 import Web3


class RpcClient:
    web3Client: Web3

    def __init__(self, rpc_url: str):
        self.web3Client = Web3(Web3.HTTPProvider(rpc_url))

    def isValid(self):
        return self.web3Client.isConnected()

    def getBalance(self, address, unit: str):
        balance = self.web3Client.eth.getBalance(address)
        return Web3.fromWei(balance, unit)

    def sendTx(self, tx: str):
        return self.web3Client.eth.sendRawTransaction(tx)

    def getTxCount(self, address):
        return self.web3Client.eth.get_transaction_count(address)


rc = RpcClient("https://eth-ropsten.alchemyapi.io/v2/KE3V4NLUN3fgvie0lbTHyQ8Q2zSSnfo2")
aa = rc.getTxCount("0x2a8808595b5fc7E3766278E9967688dc64dc00e7")
print(aa)
