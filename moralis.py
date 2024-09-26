importlib.import_module('sol_api')

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6ImVlOWFkNGM1LWIxMTgtNDgyOS04NzRjLTg5OTRlYTk4MzczOCIsIm9yZ0lkIjoiNDA5NTMzIiwidXNlcklkIjoiNDIwODQzIiwidHlwZUlkIjoiOTY0YjM2YWYtYjA0Ny00MjQ2LTg3MTctNWU1NzNmOGViZTNhIiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3MjczNTk0OTIsImV4cCI6NDg4MzExOTQ5Mn0.3I6NBMujh95Ey7cesRs8tOP_9ttOiEKHFtDMkLvaFqs"

params = {
    "address": "52C9T2T7JRojtxumYnYZhyUmrN7kqzvCLc4Ksvjk7TxD",
    "network": "mainnet",
}

result = sol_api.account.balance(
    api_key=api_key,
    params=params,
)

print(result)

