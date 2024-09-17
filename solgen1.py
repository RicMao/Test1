import base58
from solders.keypair import Keypair
from colorama import Fore

a=0
while a<=100:
        account = Keypair()
        private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
        
        print(Fore.GREEN + f"Key: {private_key}")
        print(Fore.YELLOW + f"Adr: {account.pubkey}")
        a=a+1
      
