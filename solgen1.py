import base58
from solders.keypair import Keypair
from moralis import sol_api
from colorama import Fore

a=0
while a<=10:
    # Random generate address & private key 
    account = Keypair()
    private_key = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
    address = account.pubkey()


    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjMxN2UyNjdmLTU1YmUtNGM0OS04ZTI3LTZlOWQ0YWVjZTM0OCIsIm9yZ0lkIjoiNDA4MjU5IiwidXNlcklkIjoiNDE5NTA5IiwidHlwZUlkIjoiZDRmMWJmYjAtOGNkZS00YzY2LWJiNWQtM2VmZTE5NzhmMWY0IiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3MjYyMTg5MTUsImV4cCI6NDg4MTk3ODkxNX0.C2hqVGCoHD1gYJQLX8IQVaWpLpzfEJbRuPDONVB7uck"

params = {
    "addr": "address",
    "network": "mainnet",
}

result = sol_api.account.balance(
    api_key=api_key,
    params=params,
)

    print(Fore.GREEN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(result)
    a=a+1
