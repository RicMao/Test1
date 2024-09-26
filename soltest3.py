import requests

url = "https://api.tatum.io/v3/solana/account/balance/FykfMwA9WNShzPJbbb9DNXsfgDgS3XZzWiFgrVXfWoPJ"

headers = {
    "accept": "application/json",
    "x-api-key": "t-66f3de3e6be651758a55cd61-5d1a4df4209c4956afa40401"
}

response = requests.get(url, headers=headers)

print(response.text)
