from secrets import token_bytes
from coincurve import PublicKey
from pysha3 import keccak_256
from web3 import Web3
import time
from colorama import Fore

# Create an instance of the Web3 class connected to the desired network
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/768e3814ba4c4e01a06e88765a30c551"))

# Infinite loop to continuously generate keys and check balances
while True:
    # Generate a random private key
    private_key = keccak_256(token_bytes(32)).digest()
    
    #DERIVE THE PUBLIC KEY FROM THE  PRIVATE KEY
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]

    # Derive the Ethereum address from the private key
    address = keccak_256(public_key).digest()[-20:]

    # Check the balance of the address
    balance = w3.eth.get_balance(address)

    # Convert the balance from wei to Ether
    balance_ether = w3.from_wei(balance, 'ether')

    print(Fore.GREEN + f"Key: {private_key}")
    print(Fore.WHITE + f"Adr: {address}")
    print(Fore.YELLOW + f"Eth: {balance_ether}")
    time.sleep(0.001)

    # Check if balance is above 0.001 Ether
    if balance_ether > 0.001: break
