import math
#import matplotlib.pyplot as plt
#import numpy

# wczytanie i konwersja danych
with open('SunspotData.csv','r') as f:
    lines = f.readlines()
year = []
x = []
for value in lines:
    as_list = value.split(" ")
    year.append(as_list[0])
    x.append(as_list[1].replace("\n",""))
n = len(year)
for i in range(n):
    x[i] = round(float(x[i]))
    year[i] = float(year[i])

# 1. normalizacja
max = max(x)
min = min(x)
z_nor = []
for i in range(n):
    z_nor.append(round((x[i] - min) / (max - min),2))

# 2. standaryzacja
# sigma = (suma((x_1 - x_śr)^2 + (x_2 - x_śr)^2 + ... + (x_n - x_śr)^2))/n)^0.5
# z = (x - x_śr)/sigma
z_stan = []
kwadraty_roznic = []
srednia = sum(x) / n
for i in range(n):
    kwadraty_roznic.append((x[i]-srednia)**2)
sigma = (sum(kwadraty_roznic)/n)**(0.5)

for i in range(n):
    z_stan.append((x[i]-srednia)/sigma)
# test czy suma z = 0 ?
#print(sum(z_stan))
# test: czy wariancja(z) = 1 ?
#print((numpy.std(z_stan)**2))

# 3. skalowanie exp i sigmoidą
z_exp = []
for i in range(n):
    z_exp.append(1/(1+math.exp(-x[i])))
z_sigm = []
for i in range(n):
    z_sigm.append((math.exp(x[i])-math.exp(-x[i]))/(math.exp(x[i])+math.exp(-x[i])))

# 4. ślizgająca średnia
m=3
z_av3 = [float('nan')]*(int(m/2))
for i in range(len(x)-m):
    x1 = x[i:(m+i)]
    z_av3.append(round((sum(x1) / m),2))
m=5
z_av5 = [float('nan')]*(int(m/2))
for i in range(len(x)-m):
    x1 = x[i:(m+i)]
    z_av5.append(round((sum(x1) / m),2))
m=7
z_av7 = [float('nan')]*(int(m/2))
for i in range(len(x)-m):
    x1 = x[i:(m+i)]
    z_av7.append(round((sum(x1) / m),2))

# 5. ślizgająca mediana
m=3
z_mean3 = [float('nan')]*(int(m/2))
for i in range(len(x)-m):
    x1 = x[i:(m+i)]
    x2 = sorted(x1)
    mean = x2[math.floor(m/2)]
    z_mean3.append(round(mean,2))
m=5
z_mean5 = [float('nan')]*(int(m/2))
for i in range(len(x)-m):
    x1 = x[i:(m+i)]
    x2 = sorted(x1)
    mean = x2[math.floor(m/2)]
    z_mean5.append(round(mean,2))
m=7
z_mean7 = [float('nan')]*(int(m/2))
for i in range(len(x)-m):
    x1 = x[i:(m+i)]
    x2 = sorted(x1)
    mean = x2[math.floor(m/2)]
    z_mean7.append(round(mean,2))

# 6.
m=7
z_last7 = [float('nan')]*(int(m/2))
for i in range(len(x)-m):
    x1 = x[i:(m+i)]
    x2 = sorted(x1)
    x3 = x2[2:-2]
    suma = sum(x3)
    average = suma / (m-4)
    z_last7.append(round(average,2))
m=9
z_last9 = [float('nan')]*(int(m/2))
for i in range(len(x)-m):
    x1 = x[i:(m+i)]
    x2 = sorted(x1)
    x3 = x2[2:-2]
    suma = sum(x3)
    average = suma / (m - 4)
    z_last9.append(round(average, 2))
m=11
z_last11 = [float('nan')]*(int(m/2))
for i in range(len(x)-m):
    x1 = x[i:(m+i)]
    x2 = sorted(x1)
    x3 = x2[2:-2]
    suma = sum(x3)
    average = suma / (m - 4)
    z_last11.append(round(average, 2))

lista = [year,x,z_nor,z_stan,z_exp,z_sigm,z_av3,z_av5,z_av7,z_mean3,z_mean5,z_mean7,z_last7,z_last9,z_last11]

def equalizer(years,LoL):
    for i in range(len(LoL)):
        while len(years) != len(LoL[i]):
            LoL[i].append(float('nan'))
equalizer(year,lista)

for item in lista:
    print(item)

#plt.plot(year,x,label='Liczba Wolfa')
#plt.xlabel('Lata')
#plt.ylabel('Liczba Wolfa')
#plt.title('Liczba Wolfa na przestrzeni ostatnich 40-stu lat')
#plt.plot(year,z_nor)
#plt.plot(year,z_stan)
#plt.plot(year,z_exp,label='exp')
#plt.plot(year,z_sigm,label='sigmoida')
#plt.plot(year,z_av3,label='średnia, m = 3')
#plt.plot(year,z_av5,label='średnia, m = 5')
#plt.plot(year,z_av7,label='średnia, m = 7')
#plt.plot(year,z_mean3,label='mediana, m = 3')
#plt.plot(year,z_mean5,label='mediana, m = 5')
#plt.plot(year,z_mean7,label='mediana, m = 7')
#plt.plot(year,z_last7,label='m = 7')
#plt.plot(year,z_last9,label='m = 9')
#plt.plot(year,z_last11,label='m = 11')
#plt.legend()
#plt.show()
