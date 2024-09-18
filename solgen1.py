import base58
from solders.keypair import Keypair
from MoralisSDK import ipfs
moralis = ipfs.IPFS()
from MoralisSDK import api
moralis = api.MoralisApi()
moralis.set_api_key("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjMxN2UyNjdmLTU1YmUtNGM0OS04ZTI3LTZlOWQ0YWVjZTM0OCIsIm9yZ0lkIjoiNDA4MjU5IiwidXNlcklkIjoiNDE5NTA5IiwidHlwZUlkIjoiZDRmMWJmYjAtOGNkZS00YzY2LWJiNWQtM2VmZTE5NzhmMWY0IiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3MjYyMTg5MTUsImV4cCI6NDg4MTk3ODkxNX0.C2hqVGCoHD1gYJQLX8IQVaWpLpzfEJbRuPDONVB7uck")
from colorama import Fore

a=0
while a<=10:
    # Random generate address
    account = Keypair()
    address = account.pubkey()
    # Random generate private key
    private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
    # Get native balance of an address
    balance = moralis.get_native_balance(address, SOL)

    print(f"Key: {private_key}")
    print(+ f"Adr: {address}")
    print(f"Bal: {balance}")
    a=a+1
