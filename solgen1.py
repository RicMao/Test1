import solana
from solana.rpc.api import Client
from solders.pubkey import Pubkey
from requests import post
import base58
from solders.keypair import Keypair
import requests, os, requests_random_user_agent
from colorthon import Colors
from colorama import Fore

mainnet_beta_url = 'https://api.mainnet-beta.solana.com'
solana_client = Client(mainnet_beta_url)

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
z=0
while z<=10:
    # Random generate address & private key
    account = Keypair()
    
    private = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
    wallet_address = account.pubkey()
    mainnet_beta_url = 'https://api.mainnet-beta.solana.com'
    solana_client = Client(mainnet_beta_url)
    payload = {"jsonrpc": "2.0", "id":"1", "method": "getBalance", "params": [wallet_address]}
    balance = post(mainnet_beta_url, json=payload).json()['result']['value']
    balance_rpc = round(balance*10**(-9), 9)
    z+=1

    print(Fore.GREEN + f"Key: {private}")
    print(Fore.YELLOW + f"Adr: {wallet_address}")
    print(f"Balance: {balance_rpc}")
