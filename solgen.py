import base58
from solders.keypair import Keypair

WALLETS_AMOUNT = 100

with f = open('Wallet.txt', 'w')
         
    for x in range(WALLETS_AMOUNT):
        account = Keypair()
        privateKey = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
        address = account.pubkey()

        print(f"Key: {privateKey}")
        print(f"Adr: {address}")
        
  f.write('address', 'privateKey')
  f.close()
