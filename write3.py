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
    private_key = "0x" + ''.join(random.choice('053d12be4c6a978f') for i in range(64))
    address = Account.from_key(private_key).address
    api_key = 'U96YKGE4GUAF37HYMD73QFXYUK6TXJD7JY'
    url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}'
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
    if data['status'] == '1':
            balance_ether = float(data['result']) / 10 ** 18

    print(Fore.GREEN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f"Eth: {balance_ether}")

    if balance_ether > 0.001: break
    a=a+1
