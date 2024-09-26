import TatumSDK, Network, Solana

tatum = await TatumSDK.init<Solana>({
  network: Network.SOLANA,
  apiKey: 't-66a730ccccfd17001c479705-2f597d14ad7543f289a03418',
})

res = await tatum.rpc.getBalance('8Ew6iQXcTRHAUNNu3X9VBn1g1bJkXEZJ9gFD2AGKtdPB')    
    
await tatum.destroy()
