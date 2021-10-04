import urllib.request, json, csv, sys, math

import datetime
now1 = datetime.datetime.now()

#get markets
with urllib.request.urlopen("https://bittrex.com/api/v1.1/public/getmarkets") as url:
    btc = json.loads(url.read().decode())
	
outt = open("BittrexList.txt", "w")

for y in range(0,2000):
    vol = 0
    p0 = p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = 0
    try:
        bit = btc["result"][y]["BaseCurrency"]
    except:
        break
    if bit 	== 'BTC':
        active = btc["result"][y]["IsActive"]
        if active == True:
            try:
                link = btc["result"][y]["MarketCurrency"]
            except:
                break
            print(y+1,link)
            with urllib.request.urlopen("https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-%s" %(link)) as url:
                market = json.loads(url.read().decode())
            with urllib.request.urlopen("https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-%s&type=sell" %(link)) as url:
                orders = json.loads(url.read().decode())
            iksy = market["result"][0]["OpenSellOrders"]
            if iksy > 1000:
                iksy = 1000
            for x in range(0,iksy):
                if vol <= 4:
                    volbef = vol
                    try:
                        q = orders["result"][x]["Quantity"]
                    except:
                        break
                    r = orders["result"][x]["Rate"]
                    vol = vol + q*r
                    volaft = vol
                    if volbef <= 0.1:
                        volbefflo = math.floor(volbef*10)/10
                        volaftflo = math.floor(volaft*10)/10
                        deltavol = volaftflo - volbefflo
                        if volaftflo == 0.1:
                            p0 = orders["result"][x]["Rate"]
                    if vol <= 1:
                        volbefflo = math.floor(volbef*4)/4
                        volaftflo = math.floor(volaft*4)/4
                        deltavol = volaftflo - volbefflo
                        if deltavol >= 0.24:
                            if volaftflo == 0.25:
                                p1 = orders["result"][x]["Rate"]
                            if volaftflo == 0.5:
                                p2 = orders["result"][x]["Rate"]
                            if volaftflo == 0.75:
                                p3 = orders["result"][x]["Rate"]
                            if volaftflo == 1:
                                p4 = orders["result"][x]["Rate"]				
                    else:
                        volbefflo = math.floor(volbef*2)/2
                        volaftflo = math.floor(volaft*2)/2
                        deltavol = volaftflo - volbefflo
                        if deltavol >= 0.5:
                            if volaftflo == 1:
                                p4 = orders["result"][x]["Rate"]
                            if volaftflo == 1.5:
                                p5 = orders["result"][x]["Rate"]
                            if volaftflo == 2:
                                p6 = orders["result"][x]["Rate"]
                            if volaftflo == 2.5:
                                p7 = orders["result"][x]["Rate"]
                            if volaftflo == 3:
                                p8 = orders["result"][x]["Rate"]
                            if volaftflo == 3.5:
                                p9 = orders["result"][x]["Rate"]
                            if volaftflo == 4:
                                p10 = orders["result"][x]["Rate"]
                else:
                    break						
        print("%6s"%(btc["result"][y]["MarketCurrency"]),"%12.8f"%(market["result"][0]["BaseVolume"]),"%12.8f"%(orders["result"][0]["Rate"]),"%12.8f"%(p0),"%12.8f"%(p1),"%12.8f"%(p2),"%12.8f"%(p3),"%12.8f"%(p4),"%12.8f"%(p5),"%12.8f"%(p6),"%12.8f"%(p7),"%12.8f"%(p8),"%12.8f"%(p9),"%12.8f"%(p10),file=outt)
		
now2 = datetime.datetime.now()
print("Bittrex")
print("Start:",now1.strftime("%H:%M:%S"))
print("Finish:",now2.strftime("%H:%M:%S"))

import winsound
winsound.PlaySound("sound", winsound.SND_ALIAS)