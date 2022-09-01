import json,time
from fetch_post_data import fetch_post_data
from win10toast import ToastNotifier
from fetch_gm_token_price import fetch_wax_price,fetch_gm_token_price

toaster = ToastNotifier()

with open("land_payload.json") as f:
	land_payload = json.load(f)

raw_land_data = fetch_post_data(land_payload)["rows"][0]["data"]
curr_GMM_bal = raw_land_data["r1_reward"]/10000
curr_GMF_bal = raw_land_data["r2_reward"]/10000
curr_GME_bal = raw_land_data["mr_reward"]/10000
curr_GMD_bal = raw_land_data["gmd_reward"]/10000

print(f"Current token balances are: {curr_GMM_bal} GMM, {curr_GMF_bal} GMF, {curr_GME_bal} GME, {curr_GMD_bal} GMD")
print("Listening for mines...")

while(1):
	gm_token_price_list = fetch_gm_token_price()
	wax_usd = fetch_wax_price()
	while True:
		try:
			raw_land_data = fetch_post_data(land_payload)["rows"][0]["data"]
			new_GMM_bal = raw_land_data["r1_reward"]/10000
		except:
			time.sleep(10)
			continue
		break


	if(curr_GMM_bal!=new_GMM_bal):
		GMM_comm = raw_land_data["r1_reward"]/10000 - curr_GMM_bal
		GMF_comm = raw_land_data["r2_reward"]/10000 - curr_GMF_bal
		GME_comm = raw_land_data["mr_reward"]/10000 - curr_GME_bal
		GMD_comm = raw_land_data["gmd_reward"]/10000 - curr_GMD_bal

		total_profit = ((GMM_comm*gm_token_price_list[0])+(GMF_comm*gm_token_price_list[1])+(GME_comm*gm_token_price_list[2])+(GMD_comm*gm_token_price_list[3]))*wax_usd

		toaster.show_toast(f"Someone mined in your land +${total_profit:.2f}",f"+{GMM_comm:.4f} GMM $({GMM_comm*gm_token_price_list[0]*wax_usd:.2f}) \n+{GMF_comm:.4f} GMF $({GMF_comm*gm_token_price_list[1]*wax_usd:.2f})\n+{GME_comm:.4f} GME $({GME_comm*gm_token_price_list[2]*wax_usd:.2f})\n+{GMD_comm:.4f} GMD $({GMD_comm*gm_token_price_list[3]*wax_usd:.2f})")
		
		print(f"{GMM_comm:.4f},{GMF_comm:.4f},{GME_comm:.4f},{GMD_comm:.4f}")

		curr_GMM_bal = raw_land_data["r1_reward"]/10000
		curr_GMF_bal = raw_land_data["r2_reward"]/10000
		curr_GME_bal = raw_land_data["mr_reward"]/10000
		curr_GMD_bal = raw_land_data["gmd_reward"]/10000
		total_profit = 0

	time.sleep(2)