from web3 import Web3


class RpcClient:
    web3Client: Web3

    def __init__(self, rpc_url: str):
        self.web3Client = Web3(Web3.HTTPProvider(rpc_url))

    def isValid(self):
        return self.web3Client.isConnected()

    def getBalance(self, address: str, unit: str):
        balance = self.web3Client.eth.getBalance(Web3.toChecksumAddress(address))
        return Web3.fromWei(balance, unit)

    def sendTx(self, tx: str):
        return self.web3Client.eth.sendRawTransaction(tx)

    def getTxCount(self, address):
        return self.web3Client.eth.get_transaction_count(Web3.toChecksumAddress(address))

    def getTxByHash(self, txHash):
        return self.web3Client.eth.get_transaction(txHash)

    def getTxByHashRecipt(self, txHash):
        return self.web3Client.eth.get_transaction_receipt(txHash)



