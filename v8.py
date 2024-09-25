import random
import secrets
from eth_keys import keys
from eth_account import Account
from web3 import Web3
import requests, os, requests_random_user_agent
from colorthon import Colors
from colorama import Fore
import time

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
a=0
z=1
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/39badee648694e7c9def9a93705c431c"))

while a<=10000000:
    private_key = "0x" + ''.join(random.choice('01fb234c56879ade') for i in range(64))
    address = Account.from_key(private_key).address
    balance = w3.eth.get_balance(address)
    balance_ether = w3.from_wei(balance, 'ether')

    print(f"{red}{'=' * 29}[{reset}{white}Scan-V8{reset}:{yellow}{z}{reset}{red}]{'=' * 29}{reset}")
    print(Fore.BLUE + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f"Eth: {balance_ether}")
    z+=1
    a+=1
    # ------------------------------------------------------------------------
    if balance_ether > 0.001: break
    
