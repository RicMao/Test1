import base58
from solders.keypair import Keypair
import requests, os, requests_random_user_agent
from colorthon import Colors
from colorama import Fore

def getClear():
    os.system('cls' if os.name == 'nt' else 'clear')
# ------------------------------------------------------------------------
green = Colors.GREEN
red = Colors.RED
white = Colors.WHITE
yellow = Colors.YELLOW
reset = Colors.RESET
getClear()
# ------------------------------------------------------------------------
z=1
a=0

while a>=100:
    # Random generate address & private key 
    account = Keypair()
    private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
    address = account.pubkey()
   
    print(Fore.GREEN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address} {red}[{reset}{yellow}{z}{reset}{red}]{reset}")
z=z+1
a=a+1
