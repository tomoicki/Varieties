from tkinter import *
import tkinter as tk
import numpy, pandas

Coin = numpy.loadtxt(fname = "BittrexList.txt",dtype='object,f,f,f,f,f,f,f,f,f,f,f,f,f')
CN = Coin
Rows = numpy.size(Coin,0)

for i in range(Rows):
    for j in range(11):
        CN[i][j+3] = CN[i][j+3]/CN[i][2]
        
cols = ['Name','Volume','Price','0.1BTC','0.25BTC','0.5BTC','0.75BTC','1BTC','1.5BTC','2BTC','2.5BTC','3BTC','3.5BTC','4BTC']
df = pandas.DataFrame(data=CN)
df.columns=cols
pandas.options.display.float_format = '{:6.2f}'.format
del df['Price']
button_names = cols
for i in range(3):
    del button_names[0]

sdf = [] #sorted display frames

for i in range(len(button_names)):
    sdf.append(df.sort_values(by=button_names[i], ascending=False))

def printbutton(index):
    return {
        0 : print(df.sort_values(by=button_names[0], ascending=False).head(2)),
        1 : print(df.sort_values(by=button_names[1], ascending=False).head(2)),
        2 : print(df.sort_values(by=button_names[2], ascending=False).head(2)),
        3 : print(df.sort_values(by=button_names[3], ascending=False).head(2))
    }[index]

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button_list = []
for name in button_names:
    i = 0
    b = tk.Button(frame, text = name, command = printbutton(i))
    b.pack(side=LEFT)
    i += 1
    button_list.append(b)
root.mainloop()