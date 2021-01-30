import json

with open('il.json',encoding='utf8') as f:
    veri = json.load(f)

iller=[]
ilce=[]

data=veri["iller"]

def get_il():
    for il in data.keys():
        iller.append(il)
    print(iller)


def get_ilce(il):
    for il in data[il.capitalize()]:
        ilce.append(il)
    print(ilce)

get_il()

il=input("hangi il?\n")
get_ilce(il)