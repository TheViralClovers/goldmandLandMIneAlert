import requests,json

def fetch_wax_price():
	req_url = "https://api.coingecko.com/api/v3/simple/price?ids=WAX&vs_currencies=USD%2CINR"
	raw_price_data = json.loads(requests.get(req_url).content)
	wax_usd = raw_price_data["wax"]["usd"]
	# wax_inr = raw_price_data["wax"]["inr"]
	return (wax_usd)

def fetch_gm_token_price():
	req_url = "https://wax.alcor.exchange/api/markets"
	raw_market_data = json.loads(requests.get(req_url).content)
	for market_pair in raw_market_data:
		# print(market_pair)
		if(market_pair['base_token']["symbol"]["name"] == 'WAX' and market_pair['quote_token']["symbol"]["name"]=='GMM'):
			GMM_price = market_pair["last_price"]

		if(market_pair['base_token']["symbol"]["name"] == 'WAX' and market_pair['quote_token']["symbol"]["name"]=='GMF'):
			GMF_price = market_pair["last_price"]

		if(market_pair['base_token']["symbol"]["name"] == 'WAX' and market_pair['quote_token']["symbol"]["name"]=='GME'):
			GME_price = market_pair["last_price"]

		if(market_pair['base_token']["symbol"]["name"] == 'WAX' and market_pair['quote_token']["symbol"]["name"]=='GMD'):
			GMD_price = market_pair["last_price"]
	return(GMM_price,GMF_price,GME_price,GMD_price)

# print(fetch_gm_token_price())
# print(fetch_wax_price())