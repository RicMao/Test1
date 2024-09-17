import base58
from solders.keypair import Keypair
from theblockchainapi import SolanaAPIResource, SolanaCurrencyUnit, SolanaMintAddresses, SolanaNetwork, SolanaWallet
from colorama import Fore

MY_API_KEY_ID = '4ZZZFwNf4b8bumN'
MY_API_SECRET_KEY = 'Xedr13zVPXNrFq6'

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)

        account = Keypair()
        private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
        address = account.pubkey()
        balance = BLOCKCHAIN_API_RESOURCE.get_balance(address)
        print(f"SOL Balance of {address}")
        print(balance)
      
