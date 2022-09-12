from web3 import Web3
import json


def mnemo_To_Key(mnemo):
	bsc  = "https://bsc-dataseed1.binance.org/"
	web3 = Web3(Web3.HTTPProvider(bsc))
	web3.eth.account.enable_unaudited_hdwallet_features()
	cuenta = web3.eth.account.from_mnemonic(mnemo)
	print(f'\nBackup Wallet Adress: \n{cuenta.address}')
	return({'key':str(cuenta.key),
	'address': str(cuenta.address)})



if __name__ == '__main__':
	frase = input("Ingresa la Frase para Darte una Clave Privada:\n")
	account = mnemo_To_Key(frase)
	json_object = json.dumps(account, indent=4)
	with open("account.json", "w") as jsonfile:
		jsonfile.write(json_object)
