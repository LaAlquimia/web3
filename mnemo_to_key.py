from web3 import Web3

##Hacer función que guarde la privada!!!!!


##Pendiente


def mnemo_To_Key(mnemo):
	bsc  = "https://bsc-dataseed1.binance.org/"
	web3 = Web3(Web3.HTTPProvider(bsc))
	web3.eth.account.enable_unaudited_hdwallet_features()
	cuenta = web3.eth.account.from_mnemonic(mnemo)
	return(cuenta.key)




