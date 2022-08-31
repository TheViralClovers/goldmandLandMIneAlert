import requests,json,time

with open("endpoints.json") as f:
	endpoints = json.load(f)

index = 0

def fetch_post_data(payload):
	global index
	raw_data = {}
	try:
		req_url = endpoints[0 if(index > len(endpoints) - 1)  else index] + "/v1/chain/get_table_rows"
		raw_data = json.loads(requests.post(json = payload, url = req_url).content)
	except:
		index=index+1
		return fetch_post_data(payload)
	return raw_data