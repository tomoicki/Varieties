import urllib.request, json, csv, sys, math
from ast import literal_eval

import datetime
now1 = datetime.datetime.now()

with urllib.request.urlopen("https://www.binance.com/api/v3/exchangeInfo") as url:
    btc = json.loads(url.read().decode())
	
outt = open("Binance.txt", "w")

for y in range(0,1000):
    vol = 0.0
    p0 = p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = 0
    try:
        bit = btc["symbols"][y]["quoteAsset"]
    except:
        break
    if bit 	== "BTC":
        active = btc["symbols"][y]["status"]
        if active == "TRADING":
            try:
                link = btc["symbols"][y]["symbol"]
            except:
                break
            name = btc["symbols"][y]["baseAsset"]
            with urllib.request.urlopen("https://www.binance.com/api/v3/trades?symbol=%s" %(link)) as url:
                market = json.loads(url.read().decode())
            print(y+1,name)
            with urllib.request.urlopen("https://www.binance.com/api/v3/depth?symbol=%s" %(link)) as url:
                orders = json.loads(url.read().decode())
            for x in range(1000):
                if vol <= 4:
                    volbef = vol
                    try:
                        q = orders["asks"][x][1]
                    except:
                        break
                    r = orders["asks"][x][0]
                    q = literal_eval(q)
                    r = literal_eval(r)
                    vol = vol + q*r
                    volaft = vol
                    if volbef <= 0.1:
                        volbefflo = math.floor(volbef*10)/10
                        volaftflo = math.floor(volaft*10)/10
                        deltavol = volaftflo - volbefflo
                        if volaftflo == 0.1:
                            p0 = orders["asks"][x][0]
                    if vol <= 1:
                        volbefflo = math.floor(volbef*4)/4
                        volaftflo = math.floor(volaft*4)/4
                        deltavol = volaftflo - volbefflo
                        if deltavol >= 0.24:
                            if volaftflo == 0.25:
                                p1 = orders["asks"][x][0]
                            if volaftflo == 0.5:
                                p2 = orders["asks"][x][0]
                            if volaftflo == 0.75:
                                p3 = orders["asks"][x][0]
                            if volaftflo == 1:
                                p4 = orders["asks"][x][0]				
                    else:
                        volbefflo = math.floor(volbef*2)/2
                        volaftflo = math.floor(volaft*2)/2
                        deltavol = volaftflo - volbefflo
                        if deltavol >= 0.5:
                            if volaftflo == 1:
                                p4 = orders["asks"][x][0]
                            if volaftflo == 1.5:
                                p5 = orders["asks"][x][0]
                            if volaftflo == 2:
                                p6 = orders["asks"][x][0]
                            if volaftflo == 2.5:
                                p7 = orders["asks"][x][0]
                            if volaftflo == 3:
                                p8 = orders["asks"][x][0]
                            if volaftflo == 3.5:
                                p9 = orders["asks"][x][0]
                            if volaftflo == 4:
                                p10 = orders["asks"][x][0]
                else:
                    break
        print(name,"vol",market[-1]["price"],p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,file=outt)
        
now2 = datetime.datetime.now()
print("Binance")
print("Start:",now1.strftime("%H:%M:%S"))
print("Finish:",now2.strftime("%H:%M:%S"))

import winsound
winsound.PlaySound("sound", winsound.SND_ALIAS)