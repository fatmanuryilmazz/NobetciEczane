from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import requests
from bs4 import BeautifulSoup


def url_istek_at(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    return requests.get(url, headers=headers)


def html_parse(htmlKaynak):
    return BeautifulSoup(htmlKaynak.content, "html.parser")


def get_element(source, elem, type, find):
    return source.find_all(elem, attrs={type: find})


def printer(printarr):
    for p in printarr:
        Lb1.insert(0,p.text)
        #print(p.text)


mainwin = Tk()
mainwin.title("Nobetçi Eczane")
mainwin.geometry("1000x1000")

L1 = Label(mainwin, text="İl Seçiniz:")
L1.pack(side=LEFT)
L1.place(x = 5,y = 5, width = 150, height = 50)

def ilgetir():
    with open('C:/Users/Pc/Documents/deneme/NobetciEczane/il.json') as f:
        veri = json.load(f)
        yeniveri=json.dumps(veri)
        for sehir in yeniveri:
            print(sehir)
            


n = StringVar()
cb =ttk.Combobox(mainwin, textvariable=n)
cb['values']=[ilgetir]
cb.bind('<FocusIn>', lambda event: ilgetir)
cb.pack()
cb.place(x = 200,y = 12, width = 100, height = 25)

#E1 = Entry(mainwin, bd=5)
#E1.pack(side=RIGHT)
#E1.place(x = 200,y = 12, width = 100, height = 25)

L2 = Label(mainwin, text="İlçe Seçiniz:")
L2.pack(side=LEFT)
L2.place(x = 10,y = 40, width = 150, height = 50)

E2 = Entry(mainwin, bd=5)
E2.pack(side=RIGHT)
E2.place(x = 200,y = 48, width = 100, height = 25)

def eczanelerigetir():
    il = ils.get()
    ilce = E2.get()
    url = url_istek_at("https://{}.eczaneleri.org/{}/nobetci-eczaneler.html".format(il, ilce))
    parse = html_parse(url)
    elem = get_element(parse, "li", "class", "media")
    printer(elem)

B = Button(mainwin, text="tıklayın",command=eczanelerigetir)
B.pack()
B.place(x = 100,y =100,width=100,height=50)

Lb1 = Listbox(mainwin)
Lb1.pack()
Lb1.place(x=200,y=100,width =800,height = 200)
mainwin.mainloop()









