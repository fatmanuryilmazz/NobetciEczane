import requests
from bs4 import BeautifulSoup
import json

iller = []
ilceler = []
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


def url_istek_at(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    return requests.get(url, headers=headers)


def html_parse(htmlKaynak):
    return BeautifulSoup(htmlKaynak.content, "html.parser")


def get_element(source, elem, type, find):
    return source.find_all(elem, attrs={type: find})


def printer(printarr):
    for p in printarr:
        # print(p.text)
        name = p.h4.text
        # print(name.rstrip())
        
        date = get_element(p, "span", "class", "date")
        # print(date[0].text)
        
        # TODO: Adres Eklenecek
        print(name.rstrip() + "\t" + date[0].text)



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


def ilce_getir(il):
    for il in data[il]:
        ilceler.append(il)
    print(ilceler)


def karakter_cevir(metin):
    for karakter in tr_chars:
        metin = metin.replace(karakter, tr_chars[karakter])
    return metin


print("\n\n İller Listeleniyor\n")
il_getir()
il = input("\nİl Girin: ").replace(" ","").capitalize()

print("\n\n {} İlçeleri Listeleniyor\n".format(il))
ilce_getir(il)

ilce = input("\nİlçe Girin: ").replace(" ","").capitalize()

print("\n\n {} ili {} İlçesi Nöbetçi Eczaneler Listeleniyor".format(il, ilce))
url = url_istek_at("https://{}.eczaneleri.org/{}/nobetci-eczaneler.html".format(karakter_cevir(il), karakter_cevir(ilce)))
parse = html_parse(url)
elem = get_element(parse, "div", "class", "media-body")
printer(elem)
