import solana
from solana.rpc.api import Client
from solders.pubkey import Pubkey
from requests import post

wallet_address = '52C9T2T7JRojtxumYnYZhyUmrN7kqzvCLc4Ksvjk7TxD'
mainnet_beta_url = 'https://api.mainnet-beta.solana.com'
solana_client = Client(mainnet_beta_url)

#balance = solana_client.get_balance.str(wallet_address)['result']['value']
#ui_balance = round(balance*10**(-9), 9)
#print(ui_balance)

payload = {"jsonrpc": "2.0", "id":"1", "method": "getBalance", "params": [wallet_address]}
balance = post(mainnet_beta_url, json=payload).json()['result']['value']
balance_rpc = round(balance*10**(-9), 9)
print(balance_rpc)
