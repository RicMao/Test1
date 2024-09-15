import secrets
from eth_account import Account
from web3 import Web3
import time
from colorama import Fore

# Create an instance of the Web3 class connected to the desired network
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/768e3814ba4c4e01a06e88765a30c551"))

# Infinite loop to continuously generate keys and check balances
while True:
    # Generate a random private key
    def generate_private_key():
    # Generate a random 32-byte (256-bit) private key
    private_key = secrets.token_bytes(32)
    return private_key

random_key = generate_private_key()
private_key = random_key.hex())
    
    # Derive the Ethereum address from the private key
    address = Account.from_key(private_key).address

    # Check the balance of the address
    balance = w3.eth.get_balance(address)

    # Convert the balance from wei to Ether
    balance_ether = w3.from_wei(balance, 'ether')

    print(Fore.GREEN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f"Eth: {balance_ether}")
    time.sleep(0.001)

    # Check if balance is above 0.001 Ether
    if balance_ether > 0.001: break
