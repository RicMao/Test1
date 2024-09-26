from solana.rpc.api import Client

address = '52C9T2T7JRojtxumYnYZhyUmrN7kqzvCLc4Ksvjk7TxD'
mainnet_beta_url = 'https://api.mainnet-beta.solana.com'
solana_client = Client(mainnet_beta_url)

balance = solana_client.get_balance(address)['result']['value']
ui_balance = round(balance*10**(-9), 9)
print(ui_balance)
