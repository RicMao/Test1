import bytes_string
import account_utils
import keccak_hash

private_key = keccak_hash(bytes_string(32)).digest()
public_key = account_utils(private_key).format(compressed=False)[1:]
addr = keccak_hash(public_key).digest(),-20

print(pvkey: private_key.hex())
print(Eth addr: addr.hex())
