from solana.rpc.api import Client
from requests import post

wallet_address = '52C9T2T7JRojtxumYnYZhyUmrN7kqzvCLc4Ksvjk7TxD'
mainnet_beta_url = 'https://api.mainnet-beta.solana.com'
solana_client = Client(mainnet_beta_url)

balance = solana_client.get_balance('52C9T2T7JRojtxumYnYZhyUmrN7kqzvCLc4Ksvjk7TxD')['result']['value']
ui_balance = round(balance*10**(-9), 9)
#print(ui_balance)

payload = {"jsonrpc": "2.0", "id":1, "method": "getBalance", "params: [wallet_address]}
balance_rpc = post(mainnet_beta_url, json=payload).jason()['result']['value']
ui_balance_rpc = round(balance*10**(-9), 9)
print(ui_balance_rpc)
