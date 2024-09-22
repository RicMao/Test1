from theblockchainapi import SolanaAPIResource, SolanaMintAddresses, SolanaNetwork, SolanaWallet

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = "OPN3dRG4G6KaiDo"
MY_API_SECRET_KEY = e4rgYD2nuTxZHx5

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("OPN3dRG4G6KaiDo")

    # (1) Test get SOL balance
    # Create a new wallet, get an airdrop, and then get its balance
    secret_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    print(secret_phrase)
    wallet = SolanaWallet(secret_recovery_phrase=secret_phrase)
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
    print(public_key)
    result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key)
    print(f"SOL Balance of {public_key}")
    print(result)
