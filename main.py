import asyncio 
from pancake import get_ogt_price
from balances import *
from orders import *
from config import private
import os

_address= "0xAAC2e6F716EBfA44ff953bd1D84E8122480eC629"


grid_pct = 12/100

async def main():
	orders = [0.00027,0.00023,0.00021,0.0002]
	while True :
		price = await get_ogt_price()
		balances = {
		'usdt': float(balance_usdt(_address)) ,
		'bnb' : float(balance_bnb(_address)) ,
		'ogt' : float(balance_ogt(_address)) ,
		}
		if len(orders)==0:
			return False
		os.system('clear')

		if price['price'] < orders[-1]:
			print(f"por debajo.... siguiente punto {orders[-1]}")



		if price['price'] > orders[-1]:
			#Funcion de compra Lista()
			amount = balances['ogt']*grid_pct
			minrc  = amount*price['price_BNB']*0.99 
			tkn = limit_sell(amount,minrc,_address)
			#funcion de Validación compra
			new_balance = float(balance_ogt(_address))
			if  new_balance > balances['ogt']:
				print (f"Prev. balance {balances['ogt']}\nNew Balance {new_balance}")
				orders.pop()
			else :
				print("Warning, Balance not change!")

		print(f'Balance BNB:{float(balance_bnb(_address))}')
		print(f'Balance OGT:{float(balance_ogt(_address))}')
		print(f'Balance USDT:{float(balance_usdt(_address))}')
		asyncio.sleep(0)
		

if __name__ == "__main__":
	asyncio.run(main())




