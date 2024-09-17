import base58
from solders.keypair import Keypair
from theblockchainapi import SolanaAPIResource, SolanaCurrencyUnit, SolanaMintAddresses, SolanaNetwork, SolanaWallet
from colorama import Fore

MY_API_KEY_ID = "s1hf0noqjvgHTyH"
MY_API_SECRET_KEY = "WWVuY33eR8s3sby"

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)

a=0
while a<=100:
        account = Keypair()
        private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
        address = account.pubkey()
        balance = resource.get_balance(address, unit=SolanaCurrencyUnit.sol, network=SolanaNetwork.MAINNET_BETA)
            
        print(Fore.GREEN + f"Key: {private_key}")
        print(Fore.YELLOW + f"Adr: {address}")
        print(Fore.WHITE + f"Sol: {balance}")
        a=a+1
      
