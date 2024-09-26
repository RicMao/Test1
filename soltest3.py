import requests

url = 'https://ethereum-mainnet.gateway.tatum.io/'
headers = {
  'accept': 'application/json',
  'content-type': 'application/json',
  'x-api-key': 't-66f3de3e6be651758a55cd61-5d1a4df4209c4956afa40401'
}
body = {
  'jsonrpc': '2.0',
  'method': 'eth_blockNumber',
  'id': 1
}

response = requests.post(url, headers=headers, json=body)
print(response.text)
