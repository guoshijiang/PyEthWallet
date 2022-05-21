from secp256k1 import PrivateKey
from web3 import Web3
from pybitcoin import encode_pubkey


def pubkey_to_address(pubkey):
    pubkey = encode_pubkey(pubkey, 'bin')
    pubkey = pubkey[1:]
    assert len(pubkey) == 64
    pubkey_hash = Web3.keccak(pubkey)
    addr = Web3.toHex(pubkey_hash[12:])
    assert Web3.isAddress(addr)
    return addr


def privkey_to_pubkey(privkey: str) -> str:
    privkey_obj = PrivateKey(bytes.fromhex(privkey))
    return privkey_obj.pubkey.serialize().hex()


def create_address():
    privkey = PrivateKey().serialize()
    public_key = privkey_to_pubkey(privkey)
    return {
        "privkey": privkey,
        "public_key": public_key,
        "address": pubkey_to_address(public_key)
    }

# {
#     'privkey': '59488f5fd5489d7166f6563e30fc6fcd39e08e1f3f0ccec13beba56a35920371',
#     'public_key': '03642bdc27728b31ca3c46b74380d11325b7f1a2fc8a3f395a5646700298dbf673',
#     'address': '0x26bb2fe53a40f23ec34fd15095d98a342a4d58d5'
# }
