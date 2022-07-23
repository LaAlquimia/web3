nonce = conector.eth.get_transaction_count(billetera.address)

txn = contract.functions.swapExactETHForTokens(0,[wbnb,ogt],billetera.address,(int(time.time()) + 1000)).buildTransaction({
'from': billetera.address,
'value': web3.toWei(amount,'ether'),#This is the Token(BNB) amount you want to Swap from
'gas': 250000,
'gasPrice': web3.toWei('5','gwei'),
'nonce': nonce,
})

# sign

txn_res = conector.eth.send_raw_transaction(txn.rawTransaction)