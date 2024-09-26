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
while z<=10:
    # Random generate address & private key
    account = Keypair()
    
    private = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
    #address = account.pubkey()
    address = "MJKqp326RZCHnAAbew9MDdui3iCKWco7fsK9sVuZTX2"

    url = "https://api.tatum.io/v3/solana/account/balance/{address}"
    headers = {
    "accept": "application/json",
    "x-api-key": "t-66f3de3e6be651758a55cd61-5d1a4df4209c4956afa40401"
    }
    response = requests.get(url, headers=headers)
    
    
    print(Fore.GREEN + f"Key: {private}")
    #print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f" Bal: {response}")
    
z+=1
