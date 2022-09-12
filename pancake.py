import requests as r 
import asyncio, json

async def get_ogt_price():
	resp =  r.get("https://api.pancakeswap.info/api/v2/tokens/0x598642F59c0366643C6F9ee3252cBB3Ef1524C51")
	ogt = {
	'price' : float(resp.json()['data']['price']),
	'price_BNB' : float(resp.json()['data']['price_BNB'])
	}
	return (ogt)

