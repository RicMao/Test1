
import base58
import json
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
file1=open("Sollet.txt","a")

z=0
while z<=50:
    # Random generate address & private key
    account = Keypair()
    
    private = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
    wallet_address = account.pubkey()
    z+=1

    file1.write(str(wallet_address)+"\n")
    file1.write(str(private)+"\n)

    print(Fore.GREEN + f"Key: {private}")
    print(Fore.YELLOW + f"Adr: {wallet_address}")

file1.close()

    
