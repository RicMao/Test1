from theblockchainapi import SolanaAPIResource, SolanaMintAddresses, SolanaNetwork, SolanaWallet

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = 'OPN3dRG4G6KaiDo'
MY_API_SECRET_KEY = 'e4rgYD2nuTxZHx5'

while BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(api_key_id=(MY_API_KEY_ID), api_secret_key=(MY_API_SECRET_KEY))


    # (1) Test get SOL balance
    # Create a new wallet, get an airdrop, and then get its balance
    secret_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    wallet = SolanaWallet(secret_recovery_phrase=secret_phrase)
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
    result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key)
    print(f"(Addr:{public_key})")
