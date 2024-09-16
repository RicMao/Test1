import secrets
from eth_keys import keys

a=0
while a<=1000:
   private_key = "{:064x}".format(secrets.randbits(256))
   private_key_bytes = bytes.fromhex(private_key)
   public_key_hex = keys.PrivateKey(private_key_bytes).public_key
   public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
   public_address = keys.PublicKey(public_key_bytes).to_address()

   print("Key = "+private_key+" "+"Address = "+public_address)
   a=a+1
