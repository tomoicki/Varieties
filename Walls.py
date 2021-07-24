import math, numpy, ast, pandas, jinja2, urllib.request, json, csv, sys, math, io
import tkinter as tk
from tkinter import ttk
from ast import literal_eval
from contextlib import redirect_stdout

root = tk.Tk() 

#Get Data Buttons
DataButtonsFrame = tk.Frame(root,
                            bd=1,
                            padx=10,
                            pady=10,
                            relief=tk.SUNKEN)
DataButtonsFrame.pack()
BittrexGT = tk.Checkbutton(DataButtonsFrame,
                           text="Bittrex",
                           indicatoron=0,
                           variable=var15).pack(side=tk.LEFT)
BinanceGT = tk.Checkbutton(DataButtonsFrame,
                           text="Binance",
                           indicatoron=0,
                           variable=var15).pack(side=tk.LEFT)                          
RunGT = tk.Button(DataButtonsFrame,
                  text="RUN",
                  width=10,
                  bd=3,
                  command=allya,
                  relief=tk.GROOVE).pack(side=tk.RIGHT)
                  
#DisplayWalls
DisplayWallsFrame = tk.Frame(root,
                             bd=1,
                             padx=10,
                             pady=10,
                             relief=tk.SUNKEN)
DisplayWallsFrame.pack()
RBittrex = tk.Radiobutton(DisplayWallsFrame,
                          text="Bittrex",
                          variable=RBValue,
                          tristatevalue=0,
                          value=1)
RBittrex.pack()
RBinance = tk.Radiobutton(DisplayWallsFrame,
                          text="Binance",
                          variable=RBValue,
                          tristatevalue=0,
                          value=2)
RBinance.pack()
for i in range(20):
    TOPList[i]=i+1
ComboTOPDefault = tk.StringVar(root)
ComboTOPDefault.set("TOP")
ComboTOP = ttk.Combobox(DisplayWallsFrame,
                        width=4,
                        textvariable=ComboTOPDefault,
                        values=TOPList,
                        state="readonly",
                        justify='center')
ComboTOP.pack(side=tk.RIGHT)
"""
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

df01 = df.sort_values(by='0.1BTC', ascending=False)
df025 = df.sort_values(by='0.25BTC', ascending=False)
df05 = df.sort_values(by='0.5BTC', ascending=False)
df075 = df.sort_values(by='0.75BTC', ascending=False)
df10 = df.sort_values(by='1BTC', ascending=False)
df15 = df.sort_values(by='1.5BTC', ascending=False)
df20 = df.sort_values(by='2BTC', ascending=False)
df25 = df.sort_values(by='2.5BTC', ascending=False)
df30 = df.sort_values(by='3BTC', ascending=False)
df35 = df.sort_values(by='3.5BTC', ascending=False)
df40 = df.sort_values(by='4BTC', ascending=False)
  
def sort01():
    print('\n',df01.head(20))
def sort025():
    print('\n',df025.head(20))
def sort05():
    print('\n',df05.head(20))
def sort075():
    print('\n',df075.head(20))
def sort10():
    print('\n',df10.head(20))
def sort15():
    print('\n',df15.head(20))
def sort20():
    print('\n',df20.head(20))
def sort25():
    print('\n',df25.head(20))
def sort30():
    print('\n',df30.head(20))
def sort35():
    print('\n',df35.head(20))
def sort40():
    print('\n',df40.head(20))"""
b01 = tk.Button(DisplayWallsFrame,
                text = "0.1BTC",
                command = sort01).pack(side=LEFT)
b025 = tk.Button(DisplayWallsFrame,
                 text = "0.25BTC",
                 command = sort025).pack(side=LEFT)
b05 = tk.Button(DisplayWallsFrame,
                text = "0.5BTC",
                command = sort05).pack(side=LEFT)
b075 = tk.Button(DisplayWallsFrame,
                 text = "0.75BTC",
                 command = sort075).pack(side=LEFT)
b10 = tk.Button(DisplayWallsFrame,
                text = "1BTC",
                command = sort10).pack(side=LEFT)
b15 = tk.Button(DisplayWallsFrame,
                text = "1.5BTC",
                command = sort15).pack(side=LEFT)
b20 = tk.Button(DisplayWallsFrame,
                text = "2BTC",
                command = sort20).pack(side=LEFT)
b25 = tk.Button(DisplayWallsFrame,
                text = "2.5BTC",
                command = sort25).pack(side=LEFT)
b30 = tk.Button(DisplayWallsFrame,
                text = "3BTC",
                command = sort30).pack(side=LEFT)
b35 = tk.Button(DisplayWallsFrame,
                text = "3.5BTC",
                command = sort35).pack(side=LEFT)
b40 = tk.Button(DisplayWallsFrame,
                text = "4BTC",
                command = sort40).pack(side=LEFT)
                
#Display Window
DisplayFrame = tk.Frame(root,
                        bd=1,
                        padx=10,
                        pady=10,
                        relief=tk.SUNKEN)
DisplayFrame.pack(side=tk.BOTTOM)
DisplayText = tk.Text(DisplayFrame,
                      height=25,
                      width=130)
DisplayText.pack(side=tk.LEFT)
DisplayText.tag_configure('justcenter', justify='center')
scroll = tk.Scrollbar(DisplayFrame, command=DisplayText.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
DisplayText.configure(yscrollcommand=scroll.set)
quote = """
Welcome!
"""
DisplayText.insert(tk.END, quote, 'justcenter')