import secrets
from eth_keys import keys
from eth_account import Account
from web3 import Web3
from colorama import Fore
import time

a=0
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/768e3814ba4c4e01a06e88765a30c551"))

while a<=10000000:
    private_key = secrets.token_hex(32)
    address = Account.from_key(private_key).address
    balance = w3.eth.get_balance(address)
    balance_ether = w3.from_wei(balance, 'ether')

    print(Fore.GREEN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f"Eth: {balance_ether}")
    
    if balance_ether > 0.001: break
    a=a+1
    
