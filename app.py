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


il = input("İl Girin ")
ilce = input("İlçe Girin ")

url = url_istek_at("https://{}.eczaneleri.org/{}/nobetci-eczaneler.html".format(il, ilce))
parse = html_parse(url)
elem = get_element(parse, "li", "class", "media")
printer(elem)