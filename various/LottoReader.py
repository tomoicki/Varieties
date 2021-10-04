import pandas
import numpy


pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify','center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)

primes = []
for num in range(1000):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                primes.append(num)

data = pandas.read_csv('Lotto5.csv',index_col='5')
data['Suma wszystkich'] = data.loc[:,'L1':'L6'].sum(axis=1)
data.rename(columns={'Dzien':'day','Miesiac':'month','Rok':'year'},inplace=True)
data['Data'] = pandas.to_datetime(data.loc[:,'day':'year'],format='%d%m%Y')
data.rename(columns={'day':'Dzien','month':'Miesiac','year':'Rok'},inplace=True)
data['Roznica dni'] = ''
for i in set(data.index.values):
    data.loc[i,'Suma duplikatow'] = sum(set(data.loc[i,'L1':'L6'].values[0])&set(data.loc[i,'L1':'L6'].values[1]))
    a = numpy.diff(data.loc[i, 'Data'].values) / 1000000000 / 60 / 60 / 24
    data.loc[i,'Roznica dni'].iloc[0] = a.tolist()
data['Suma duplikatow'] = data['Suma duplikatow'].apply(int)
for i in range(data.index.size-1):
    if data.iloc[i].name == data.iloc[i+1].name:
        temp = [str(item) for item in data.iloc[i,12]]
        data.iloc[i,12] = ' '.join(temp)
for i in range(data.index.size-1):
    if data.iloc[i].name == data.iloc[i+1].name:
        if data.iloc[i + 1, 12] == '':
            data.iloc[i + 1, 12] = data.iloc[i,12]
data.reset_index(inplace=True)
for i in range(data.index.size):
    for prime in primes:
        if (data.loc[i,'Suma wszystkich'] % prime) == 0:
            data.loc[i,'Dzielnik sumy wszystkich (pierwsza)'] = prime
            break
for i in range(data.index.size):
    for prime in primes:
        if (data.loc[i,'Suma duplikatow'] % prime) == 0:
            data.loc[i,'Dzielnik sumy duplikatow (pierwsza)'] = prime
            break
data['Dzielnik sumy duplikatow (pierwsza)'] = data['Dzielnik sumy duplikatow (pierwsza)'].astype('Int64')
data['Dzielnik sumy wszystkich (pierwsza)'] = data['Dzielnik sumy wszystkich (pierwsza)'].astype('Int64')
print(data)