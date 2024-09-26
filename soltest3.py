import requests

url = 'https://solana-mainnet.gateway.tatum.io/'
headers = {
  'accept': 'application/json',
  'content-type': 'application/json',
  'x-api-key': 't-66a730ccccfd17001c479705-2f597d14ad7543f289a03418'
}
body = {
  'jsonrpc': '2.0',
  'method': 'getVersion',
  'id': 1
}

response = requests.post(url, headers=headers, json=body)
print(response.text)
