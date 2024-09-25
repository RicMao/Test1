import web3
import requests, os, requests_random_user_agent
import time


url = "https://api.tatum.io/v3/solana/account/balance/8BseXT9EtoEhBTKFFYkwTnjKSUZwhtmdKY2Jrj8j45Rt"

headers = {
    "accept": "application/json",
    "x-api-key": "t-66a730ccccfd17001c479705-2f597d14ad7543f289a03418"
}
response = requests.get(url)
balance = response.text

print(f" Sol: {balance}")
