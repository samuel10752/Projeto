import requests
import json
#
#meses=input('nº de meses:  ')
#requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/BTC-BRL/{meses*30}')
#print(requisicao)
#cotacao = requisicao.json()
#print(cotacao)
#mb=0
#for i in cotacao:
#    #mb = (mb+float(i['bid']))//len(cotacao)
#    print(i['bid'])


meses=input('nº de meses:  ')
requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/EUR-BRL/{meses*30}')
cotacao = requisicao.json()
me=0
n=0
for i in cotacao:
    if len(str(i['bid']))==6:
        print(i['bid'])
        n=n+1
        me=me+float(i['bid'])
print(me/n)

requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/USD-BRL/90')
cotacao = requisicao.json()
d3=0
for i in cotacao:
    d3 = d3+float(i['bid'])
print(d3/len(cotacao))
