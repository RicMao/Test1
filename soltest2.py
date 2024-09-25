from solana.rpc.api import Client
import PublicKey
solana_client = Client("https://docs-demo.solana-mainnet.quiknode.pro/")
print(solana_client.get_balance(PublicKey('7cVfgArCheMR6Cs4t6vz5rfnqd56vZq4ndaBrY5xkxXy')))
