from tkinter import *
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
        print(p.text)

elem = get_element(parse, "div", "class", "media-body")



mainwin = Tk()
mainwin.title("Nobetçi Eczane")
mainwin.geometry("600x400")

L1 = Label(mainwin, text="İl Seçiniz:")
L1.pack(side=LEFT)
L1.place(x = 5,y = 5, width = 150, height = 50)

E1 = Entry(mainwin, bd=5)
E1.pack(side=RIGHT)
E1.place(x = 200,y = 12, width = 100, height = 25)

L2 = Label(mainwin, text="İlçe Seçiniz:")
L2.pack(side=LEFT)
L2.place(x = 10,y = 40, width = 150, height = 50)

E2 = Entry(mainwin, bd=5)
E2.pack(side=RIGHT)
E2.place(x = 200,y = 48, width = 100, height = 25)

il = E1.get()
ilce = E2.get()
url = url_istek_at("https://{}.eczaneleri.org/{}/nobetci-eczaneler.html".format(il, ilce))
parse = html_parse(url)


Lb1 = Listbox(mainwin)

Lb1.insert(0, elem)
Lb1.pack()
Lb1.place(x = 100,y =100,width =200,height = 200)



mainwin.mainloop()







