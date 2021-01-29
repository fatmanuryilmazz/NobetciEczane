import json

with open('il.json',encoding='utf8') as f:
    veri = json.load(f)

il=input("hangi il?\n")


data=veri["iller"][il.capitalize()]

ilce=[]
for il in data:
    ilce.append(il)
print(ilce)
