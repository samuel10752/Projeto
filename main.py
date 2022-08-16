import requests
import json

requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/USD-BRL/90')
cotacao = requisicao.json()
d3=0
for i in cotacao:
    d3 = d3+float(i['bid'])
print(d3/len(cotacao))
