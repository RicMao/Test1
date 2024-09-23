import hashlib
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
while a<=1000000:
    private_key = ''.join(random.choice('05d12b3e4c6a789f') for i in range(64))
    keccak = hashlib.sha3_256()
    keccak.update(private_key.encode())
    keccak_digest = keccak.hexdigest()
    eth_address = "0x" + keccak_digest[-20:]
    api_key = 'WXWU1HKNC5VTA3R2C2GSXSFA9X28G1I7M2'
    url = f'https://api.etherscan.io/api?module=account&action=balance&address={eth_address}&tag=latest&apikey={api_key}
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
    if data['status'] == '1':
            balance_ether = float(data['result']) / 10 ** 18

    print(Fore.CYAN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f"Eth: {balance_ether}")

    if balance_ether > 0.001: break
    a=a+1
