import base58
from solders.keypair import Keypair
from theblockchainapi import SolanaAPIResource, SolanaCurrencyUnit, SolanaMintAddresses, SolanaNetwork, SolanaWallet
from colorama import Fore

API_KEY = "s1hf0noqjvgHTyH"
SECRET_KEY = "WWVuY33eR8s3sby"

resource = SolanaAPIResource(api_key_id=API_KEY, api_secret_key=SECRET_KEY)

a=0
while a<=100:
        account = Keypair()
        private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
        address = str(account.pubkey()).decode('utf-8')
        balance = resource.get_balance(address, unit=SolanaCurrencyUnit.SOL, network=SolanaNetwork.MAINNET_BETA)
            
        print(Fore.GREEN + f"Key: {private_key}")
        print(Fore.YELLOW + f"Adr: {address}")
        print(Fore.WHITE + f"Sol: {balance}")
        a=a+1
      
