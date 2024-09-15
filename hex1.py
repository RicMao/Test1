import secrets
from eth_account import Account
from web3 import Web3
import time
from colorama import Fore

# Create an instance of the Web3 class connected to the desired network
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/768e3814ba4c4e01a06e88765a30c551"))

def generate_private_key():
    # Generate a random 32-byte (256-bit) private key
    private_key = secrets.token_bytes(32)
    return private_key

private_key = generate_private_key()
print("Private_Key :",private_key.hex())

