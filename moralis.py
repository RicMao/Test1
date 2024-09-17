from moralis import sol_api
api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "address": "BWeBmN8zYDXgx2tnGj72cA533GZEWAVeqR9Eu29txaen",
}
result = sol_api.account.get_portfolio(
    api_key=api_key,
    params=params,
)
print(result)
