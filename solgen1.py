import base58
from solders.keypair import Keypair
from colorama import Fore


a=0
filename = 'woles.txt'
outfile = open(filename, 'w')
while a<=10:
    # Random generate address & private key 
    account = Keypair()
    private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
    address = account.pubkey()
    
    print(Fore.GREEN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
a=a+1
outfile.write("Key: {private_key} + Adr: {address}\n")
outfile.close() #Close the file when we’re done!

