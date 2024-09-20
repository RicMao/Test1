from hdwallet import HDWallet
from hdwallet.symbols import BTC, ETH
import random
import requests, os, requests_random_user_agent
import secrets
from eth_keys import keys
from eth_account import Account
from web3 import Web3
from colorama import Fore
import time, re, platform

a=0
def ethBal(addr: str):
    url = f"https://ethbook.guarda.co/api/v2/address/{addr}"
    req = requests.get(url)
    if req.status_code == 200:
        ret = int(dict(req.json())['balance'])
        return ret / 1000000000000000000
    else:
        return 0
        time.sleep(0.001)

while a<=1000:
    private_key = ''.join(random.choice('0d12b3e45c6a78f9') for i in range(64))
    #address = Account.from_key(private_key).address
    address = 0x2D8c726B77a977aEc5D739eA2131941F61ECF116
    balance_ether = ethBal(address)

    print(Fore.GREEN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f"Eth: {balance_ether}")

    if balance_ether > 0.001: break
    a=a+1
    
