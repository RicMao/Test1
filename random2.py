import random
import secrets
from eth_keys import keys
from eth_account import Account
from web3 import Web3
from colorama import Fore
import time

a=0
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/1ff514bdaa0a4d02a05ab4642b1205e7"))

while a<=10000000:
    private_key = ''.join(random.choice('01fb234c56789ade') for i in range(64))
    address = Account.from_key(private_key).address
    balance = w3.eth.get_balance(address)
    balance_ether = w3.from_wei(balance, 'ether')

    print(Fore.RED + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f"Eth: {balance_ether}")
    
    f = open("hack2.txt","w")
    if balance_ether > 0.001: 
       f.write(private_key)
       f.write(address)
       f.close()
       break
    a=a+1
