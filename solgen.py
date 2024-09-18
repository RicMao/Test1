import base58
from solders.keypair import Keypair
import csv

WALLETS_AMOUNT = 5000

with open("wallets.txt", 'w', newline='') as txtfile:
    txt_writer = txt.writer(txtfile)
    txt_writer.writerow(["WALLET", "PRIVATE KEY"])

    for x in range(WALLETS_AMOUNT):
        account = Keypair()
        privateKey = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
        address = account.pubkey()
  
        txt_writer.writerow([address, privateKey])
