from tkinter import Label, Tk, ttk
from bs4 import BeautifulSoup
from datetime import datetime
from tkinter import *
from tkinter.ttk import *

import requests
import json

iller = list()
ilceler = list()
tr_chars = {
    "ç": "c",
    "Ç": "C",
    "ğ": "g",
    "Ğ": "G",
    "ı": "i",
    "İ": "I",
    "ö": "o",
    "Ö": "O",
    "ş": "s",
    "Ş": "S",
    "ü": "u",
    "Ü": "U",
}

with open("il.json", encoding="utf8") as f:
    veri = json.load(f)
    data = veri["iller"]


def il_getir():
    for il in data.keys():
        iller.append(il)
    # print(iller)


def ilce_getir(il):
    ilceler.clear()
    for il in data[il]:
        ilceler.append(il)
    # print(ilceler)


def karakter_cevir(metin):
    for karakter in tr_chars:
        metin = metin.replace(karakter, tr_chars[karakter])
    return metin


def url_istek_at(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        print("Bağlantı Hatası")


def html_parse(htmlKaynak):
    return BeautifulSoup(htmlKaynak.content, "html.parser")


def get_element(source, elem, type, find):
    return source.find_all(elem, attrs={type: find})


def printer(printarr):
    for p in printarr:
        adres=p.div.text
        listbox.insert(0,adres.rstrip())

       # date = get_element(p, "span", "class", "date")
        #print(date)


class App(ttk.Frame):
    il_combo: ttk.Combobox
    ilce_combo: ttk.Combobox

    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        il_getir()

        il_label = Label(app, text="İl Seçin")
        il_label.place(x=25, y=25, width=50)

        self.il_combo = ttk.Combobox(app)
        self.il_combo.place(x=80, y=25)
        self.il_combo["values"] = iller

        ilce_label = Label(app, text="İlçe Seçin")
        ilce_label.place(x=25, y=60, width=50)

        self.ilce_combo = ttk.Combobox(app)
        self.ilce_combo.place(x=80, y=60)

        self.il_combo.bind("<<ComboboxSelected>>", lambda event: self.change(self.il_combo.get()))

        button = ttk.Button(app, text="Tıklayın", command=self.get_eczane)
        button.place(x=75, y=100, width=100, height=50)

    def change(self, il):
        ilce_getir(il)
        self.ilce_combo.configure(values=ilceler)

    def get_eczane(self):
        il = self.il_combo.get()
        ilce = self.ilce_combo.get()
        url = url_istek_at("https://{}.eczaneleri.org/{}/nobetci-eczaneler.html".format(karakter_cevir(il), karakter_cevir(ilce)))
        # print(url)
        parse = html_parse(url)
        elem = get_element(parse, "li", "class", "media")
        printer(elem)

app = Tk()
app.title("Nöbetçi Eczane")
app.geometry("900x500")

listbox = Listbox(app)
listbox.place(x=75, y=150, width=800, height=400)

app = App(app)
app.grid(column=0, row=0, sticky="WESN")
app.mainloop()
