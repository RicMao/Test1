import secrets

def generate_private_key():
    # Generate a random 32-byte (256-bit) private key
    private_key = secrets.token_bytes(32)
    return private_key

private_key = generate_private_key()
print("Generated Private Key:", private_key.hex())

import base58
import hashlib

def hex_to_wif(hex_private_key):
    # Add the prefix byte '80' to indicate the mainnet private key
    extended_key = '80' + hex_private_key
    
    # Double SHA-256 hash the extended private key
    first_hash = hashlib.sha256(bytes.fromhex(extended_key)).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    
    # Take the first 4 bytes of the second hash as checksum
    checksum = second_hash[:4]
    
    # Add the checksum to the end of the extended private key
    extended_key += checksum.hex()
    
    # Encode the extended private key with base58 encoding
    wif = base58.b58encode(bytes.fromhex(extended_key)).decode()
    
    return wif

wif = hex_to_wif(private_key.hex())
print("Converted HEX to WIF:", wif)
