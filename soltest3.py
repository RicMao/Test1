import requests

url = "https://api.tatum.io/v3/solana/account/balance/address"

headers = {
    "accept": "application/json",
    "x-api-key": "t-66a730ccccfd17001c479705-2f597d14ad7543f289a03418"
}

response = requests.get(url, headers=headers)

print(response.text)
