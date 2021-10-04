from tkinter import *
import tkinter as tk
import numpy, ast, pandas, jinja2

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

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
             
    def create_widgets(self):
        self.b01 = tk.Button(self)
        self.b01["text"] = "0.1BTC"
        self.b01["command"] = self.sort01
        self.b01.pack(side="left")
        self.b025 = tk.Button(self)
        self.b025["text"] = "0.25BTC"
        self.b025["command"] = self.sort025
        self.b025.pack(side="left")
        self.b05 = tk.Button(self)
        self.b05["text"] = "0.5BTC"
        self.b05["command"] = self.sort05
        self.b05.pack(side="left")
        self.b075 = tk.Button(self)
        self.b075["text"] = "0.75BTC"
        self.b075["command"] = self.sort075
        self.b075.pack(side="left")
        self.b10 = tk.Button(self)
        self.b10["text"] = "1BTC"
        self.b10["command"] = self.sort10
        self.b10.pack(side="left")
        self.b15 = tk.Button(self)
        self.b15["text"] = "1.5BTC"
        self.b15["command"] = self.sort15
        self.b15.pack(side="left")
        self.b20 = tk.Button(self)
        self.b20["text"] = "2BTC"
        self.b20["command"] = self.sort20
        self.b20.pack(side="left")
        self.b25 = tk.Button(self)
        self.b25["text"] = "2.5BTC"
        self.b25["command"] = self.sort25
        self.b25.pack(side="left")
        self.b30 = tk.Button(self)
        self.b30["text"] = "3BTC"
        self.b30["command"] = self.sort30
        self.b30.pack(side="left")
        self.b35 = tk.Button(self)
        self.b35["text"] = "3.5BTC"
        self.b35["command"] = self.sort35
        self.b35.pack(side="left")
        self.b40 = tk.Button(self)
        self.b40["text"] = "4BTC"
        self.b40["command"] = self.sort40
        self.b40.pack(side="left")
    
    def sort01(self):
        print("\n")
        print(df01.head(20))
    def sort025(self):
        print("\n")
        print(df025.head(20))
    def sort05(self):
        print("\n")
        print(df05.head(20))
    def sort075(self):
        print("\n")
        print(df075.head(20))
    def sort10(self):
        print("\n")
        print(df10.head(20))
    def sort15(self):
        print("\n")
        print(df15.head(20))
    def sort20(self):
        print("\n")
        print(df20.head(20))
    def sort25(self):
        print("\n")
        print(df25.head(20))
    def sort30(self):
        print("\n")
        print(df30.head(20))
    def sort35(self):
        print("\n")
        print(df35.head(20))
    def sort40(self):
        print("\n")
        print(df40.head(20))

root = tk.Tk()
app = Application(master=root)
app.mainloop()