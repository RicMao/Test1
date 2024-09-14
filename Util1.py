from secret import token_bytes
from eth_keys import keys
from eth_utils import decode_hex, encode_hex, keccak
from web3 import Web3
import time
from colorama import Fore

# Create an instance of the Web3 class connected to the desired network
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/768e3814ba4c4e01a06e88765a30c551"))

def private_key_to_address(private_key_hex):
    # Ensure the private key is a valid hex string
    if private_key_hex.startswith('0x'):
        private_key_hex = private_key_hex[2:]
    
    # Convert the hex private key to bytes
    private_key_bytes = bytes.fromhex(private_key_hex)
    
    # Create a PrivateKey object
    private_key = keys.PrivateKey(private_key_bytes)
    
    # Derive the public key from the private key
    public_key = private_key.public_key
    
    # Get the public key bytes and skip the first byte (which is 0x04)
    public_key_bytes = public_key.to_bytes()[1:]
    
    # Compute the Keccak-256 hash of the public key bytes
    keccak_hash = keccak(public_key_bytes)
    
    # The Ethereum address is the last 20 bytes of this hash
    address_bytes = keccak_hash[-20:]
    
    # Convert the address bytes to a hexadecimal string and prepend '0x'
    address = '0x' + address_bytes.hex()
    return address

# Example usage
private_key_hex = '0x0000000000000000000000000000000000000000000000000000000000000001'
eth_address = private_key_to_address(private_key_hex)
print("Ethereum Address:", eth_address)
