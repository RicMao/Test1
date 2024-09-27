from requests import post
import solana
from solders.pubkey import Pubkey
from simplejson import JSONDecodeError
import json
import random
import base58


key_array = [4,182,130,247,119,117,227,207,112,73,170,126,222,197,244,99,215,107,255,202,33,43,36,17,104,111,157,246,196,192,174,95,240,23,238,206,118,215,154,238,229,96,11,37,156,123,51,223,5,231,17,117,86,136,103,14,75,95,175,132,148,54,1,46]
random_array = random.choices(key_array, k=64)
secret_key = random_array[0:64]
public_key = random_array[32:64]

sk = base58.b58encode(bytes(secret_key))
pk = base58.b58encode(bytes(public_key))

mainnet_beta_url = 'https://api.mainnet-beta.solana.com'
payload = {"jsonrpc": "2.0", "id":"1", "method": "getBalance", "params": ["pk"]}
balance = post(mainnet_beta_url, json=payload).json()['result']['value']
balance_rpc = round(balance*10**(-9), 9)

print(sk)
print(pk)
print(balance_rpc)
