from theblockchainapi import SolanaAPIResource, SolanaMintAddresses, SolanaNetwork, SolanaWallet

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = '4ZZZFwNf4b8bumN'
MY_API_SECRET_KEY = 'Xedr13zVPXNrFq6'

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)

    # (1) Test get SOL balance
    # Create a new wallet, get an airdrop, and then get its balance
    secret_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    print(secret_phrase)
    wallet = SolanaWallet(secret_recovery_phrase=secret_phrase)
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
    print(public_key)
    airdrop_tx_signature = BLOCKCHAIN_API_RESOURCE.get_airdrop(public_key)
    print(airdrop_tx_signature)
    result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key)
    print(f"SOL Balance of {public_key}")
    print(result)
