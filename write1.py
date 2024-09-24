from hdwallet import HDWallet
from hdwallet.symbols import BTC, ETH
import random
import requests, os, requests_random_user_agent
import secrets
from eth_keys import keys
from eth_account import Account
from web3 import Web3
from colorama import Fore
from colorthon import Colors
import time, re, platform

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
def ethBal(address: str):
    url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=("WXWU1HKNC5VTA3R2C2GSXSFA9X28G1I7M2")'
    req = requests.get(url)
   if req.status_code == 200:
       ret = int(dict(req.json())['balance'])
       return ret / 1000000000000000000
    else:
        return 0
a=0
z=1
ff=0
while a<=1000000:
    private_key = "0x" + ''.join(random.choice('053d12be4c6a978f') for i in range(64))
    address = Account.from_key(private_key).address
    balance_ether = ethBal(address)
    # ------------------------------------------------------------------------
    getClear()

    print(
        f"        {red}{'=' * 20}[{reset}{white}Scan{reset}:{yellow}{z}{reset} {white}Found{reset}: {green}{ff}{reset}{red}]{'=' * 20}{reset}")
    print(Fore.CYAN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f"Eth: {balance_ether}")

    if balance_ether > 0.001:
    ff+=1
    else: break
    
z+=1
a=a+1
