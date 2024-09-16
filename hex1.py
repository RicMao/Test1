import secrets

#generate random hex 64bytes
private_key = secrets.token_hex(nbytes=64)
print(f"PV : (private_key)")
