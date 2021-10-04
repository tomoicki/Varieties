import urllib.request, json, csv, sys, math

import datetime
now1 = datetime.datetime.now()

with urllib.request.urlopen("https://www.cryptopia.co.nz/api/GetMarkets/BTC") as url:
    btc = json.loads(url.read().decode())
	
outt = open("CryptopiaList.txt", "w")

for y in range(0,800):
	e = 0
	p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = 0
	vol = btc["Data"][y]["BaseVolume"]
	if vol != 0:
		link = btc["Data"][y]["TradePairId"]
		print(y+1,link)
		with urllib.request.urlopen("https://www.cryptopia.co.nz/api/GetMarketOrderGroups/%s/200" %(link)) as url:
			data = json.loads(url.read().decode())
		for x in range(0,200):
			if e <= 1.5:
				z = data["Data"][0]["Sell"][x]["Total"]
				ebef = e
				e = e + z
				eaft = e
				if ebef <= 0.01:
					ebefflo = math.floor(ebef*100)/100
					eaftflo = math.floor(eaft*100)/100
					deltae = eaftflo - ebefflo
					if eaftflo == 0.01:
						p1 = data["Data"][0]["Sell"][x]["Price"]
				if e <= 0.05:
					if e > 0.01:
						ebefflo = math.floor(ebef*40)/40
						eaftflo = math.floor(eaft*40)/40
						deltae = eaftflo - ebefflo
						if deltae >= 0.024:
							if eaftflo == 0.025:
								p2 = data["Data"][0]["Sell"][x]["Price"]
							if eaftflo == 0.05:
								p3 = data["Data"][0]["Sell"][x]["Price"]
				if e <= 0.2:
					if e > 0.025:
						ebefflo = math.floor(ebef*20)/20
						eaftflo = math.floor(eaft*20)/20
						deltae = eaftflo - ebefflo
						if deltae >= 0.04:
							if eaftflo == 0.05:
								p3 = data["Data"][0]["Sell"][x]["Price"]
							if eaftflo == 0.1:
								p4 = data["Data"][0]["Sell"][x]["Price"]
							if eaftflo == 0.15:
								p5 = data["Data"][0]["Sell"][x]["Price"]
				if e <= 1:
					if e > 0.2:
						ebefflo = math.floor(ebef*4)/4
						eaftflo = math.floor(eaft*4)/4
						deltae = eaftflo - ebefflo
						if deltae >= 0.25:
							if eaftflo == 0.25:
								p6 = data["Data"][0]["Sell"][x]["Price"]
							if eaftflo == 0.5:
								p7 = data["Data"][0]["Sell"][x]["Price"]
							if eaftflo == 0.75:
								p8 = data["Data"][0]["Sell"][x]["Price"]
							if eaftflo == 1:
								p9 = data["Data"][0]["Sell"][x]["Price"]								
				else:
					if e > 1:
						ebefflo = math.floor(ebef*2)/2
						eaftflo = math.floor(eaft*2)/2
						deltae = eaftflo - ebefflo
						if deltae >= 0.5:
							if eaftflo == 1:
								p9 = data["Data"][0]["Sell"][x]["Price"]
							if eaftflo == 1.5:
								p10 = data["Data"][0]["Sell"][x]["Price"]
			else:
				break
	print(btc["Data"][y]["Label"],btc["Data"][y]["TradePairId"],btc["Data"][y]["BaseVolume"],btc["Data"][y]["AskPrice"],p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,file=outt)			
	halt = btc["Data"][y]["TradePairId"]
	if halt == 4986:
		break

now2 = datetime.datetime.now()
print("Cryptopia")
print("Start:",now1.strftime("%H:%M:%S"))
print("Finish:",now2.strftime("%H:%M:%S"))

import winsound
winsound.PlaySound("sound", winsound.SND_ALIAS)