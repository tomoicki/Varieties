import numpy, ast, pandas
from pprint import pprint
import inquirer

Coin = numpy.loadtxt(fname = "BittrexList.txt",dtype='object,f,f,f,f,f,f,f,f,f,f,f,f,f')
CN = Coin
Rows = numpy.size(Coin,0)

for i in range(Rows):
    for j in range(11):
        CN[i][j+3] = CN[i][j+3]/CN[i][2]
        
cols = ['Name','Volume','Price','0.1BTC','0.25BTC','0.5BTC','0.75BTC','1BTC','1.5BTC','2BTC','2.5BTC','3BTC','3.5BTC','4BTC']
df = pandas.DataFrame(data=CN)
df.columns=cols
pandas.options.display.float_format = '{:.2f}'.format
del df['Price']

while True:
    questions = [
        inquirer.List(
            "size",
            #message="Sort by what?",
            choices=['Exit','0.10 BTC','0.25 BTC','0.50 BTC','0.75 BTC','1.00 BTC','1.50 BTC','2.00 BTC','2.50 BTC','3.00 BTC','3.50 BTC','4.00 BTC'],
        ),
    ]

    answers = inquirer.prompt(questions)
    #pprint(answers)
    if answers == {'size': 'Exit'}:
        break
    if answers == {'size': '0.10 BTC'}:
        df = df.sort_values(by='0.1BTC', ascending=False)
        print("\t\t\t\t\t\t0.1BTC\n")
        print(df.head(20))
    if answers == {'size': '0.25 BTC'}:
        df = df.sort_values(by='0.25BTC', ascending=False)
        print("\t\t\t\t\t\t0.25BTC\n")
        print(df.head(20))
    if answers == {'size': '0.50 BTC'}:
        df = df.sort_values(by='0.5BTC', ascending=False)
        print("\t\t\t\t\t\t0.5BTC\n")
        print(df.head(20))
    if answers == {'size': '0.75 BTC'}:
        df = df.sort_values(by='0.75BTC', ascending=False)
        print("\t\t\t\t\t\t0.75BTC\n")
        print(df.head(20))
    if answers == {'size': '1.00 BTC'}:
        df = df.sort_values(by='1BTC', ascending=False)
        print("\t\t\t\t\t\t1BTC\n")
        print(df.head(20))
    if answers == {'size': '1.50 BTC'}:
        df = df.sort_values(by='1.5BTC', ascending=False)
        print("\t\t\t\t\t\t1.5BTC\n")
        print(df.head(20))
    if answers == {'size': '2.00 BTC'}:
        df = df.sort_values(by='2BTC', ascending=False)
        print("\t\t\t\t\t\t2BTC\n")
        print(df.head(20))
    if answers == {'size': '2.50 BTC'}:
        df = df.sort_values(by='2.5BTC', ascending=False)
        print("\t\t\t\t\t\t2.5BTC\n")
        print(df.head(20))
    if answers == {'size': '3.00 BTC'}:
        df = df.sort_values(by='3BTC', ascending=False)
        print("\t\t\t\t\t\t3BTC\n")
        print(df.head(20))
    if answers == {'size': '3.50 BTC'}:
        df = df.sort_values(by='3.5BTC', ascending=False)
        print("\t\t\t\t\t\t3.5BTC\n")
        print(df.head(20))
    if answers == {'size': '4.00 BTC'}:
        df = df.sort_values(by='4BTC', ascending=False)
        print("\t\t\t\t\t\t4BTC\n")
        print(df.head(20))