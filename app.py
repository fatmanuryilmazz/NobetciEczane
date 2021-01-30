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


def il_getir():
    for il in data.keys():
        iller.append(il)
    print(iller)


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
