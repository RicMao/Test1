from ape import networks
web3 = networks.provider._web3


print(web3.solidity_keccak(["uint8"], [0]).hex())
print(web3.keccak(0).hex())
