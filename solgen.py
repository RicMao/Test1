import base58
from solders.keypair import Keypair
import csv

WALLETS_AMOUNT = 1000

with open("wallets.csv", 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    for x in range(100):
        account = Keypair()
        privateKey = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
        address = account.pubkey()
    
    print(f"Key: {privateKey}")
    print(f"Adr: {address}")

    csv_writer.writerow([address, privateKey])
