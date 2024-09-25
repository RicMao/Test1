import web3
import requests, os, requests_random_user_agent
import time


url = "https://api.tatum.io/v3/solana/account/balance/8BseXT9EtoEhBTKFFYkwTnjKSUZwhtmdKY2Jrj8j45Rt"

response = requests.get(url, headers=headers)
balance = response.text

print(f" Sol: {balance}")
