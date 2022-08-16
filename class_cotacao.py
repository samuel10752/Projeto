import requests
import json

class Cotacao:
    def __init__(self, d='',e='',l='',b='',et='', d3='',e3='',l3='',b3='',et3='',md='',me='',ml='',mb='',met=''):
        self.d = d
        self.e = e
        self.l = l
        self.b = b
        self.et = et
        self.d3 = d3
        self.e3 = e3
        self.l3 = l3
        self.b3 = b3
        self.et3 = et3
        self.md = md
        self.me = me
        self.ml = ml
        self.mb = mb
        self.met = met

#VALOR ESTÁTICO
    def dolar(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/all/USD-BRL')
        cotacao = requisicao.json()
        self.d=cotacao['USD']['bid']
        #print(self.x)
#VALOR ESTÁTICO
    def euro(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/all/EUR-BRL')
        cotacao = requisicao.json()
        self.e=cotacao['EUR']['bid']
#VALOR ESTÁTICO
    def libra(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/all/GBP-BRL')
        cotacao = requisicao.json()
        self.l=cotacao['GBP']['bid']
#VALOR ESTÁTICO
    def bitcoin(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/all/BTC-BRL')
        cotacao = requisicao.json()
        self.b=cotacao['BTC']['bid']
#VALOR ESTÁTICO
    def ethereum(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/all/ETH-BRL')
        cotacao = requisicao.json()
        self.et=cotacao['ETH']['bid'] 

#VALOR DOS ÚLTIMOS 3 MESES
    def dolar1(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/USD-BRL/90')
        cotacao = requisicao.json()
        self.d3=0
        for i in cotacao:
            self.d3 = (self.d3+float(i['bid']))/len(cotacao)
        
#VALOR DOS ÚLTIMOS 3 MESES  
    def euro1(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/EUR-BRL/90')
        cotacao = requisicao.json()
        self.e3=0
        for i in cotacao:
            self.e3 = (self.e3+float(i['bid']))/len(cotacao)
#VALOR DOS ÚLTIMOS 3 MESES
    def libra1(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/GBP-BRL/90')
        cotacao = requisicao.json()
        self.l3=0
        for i in cotacao:
            self.l3 = self.l3+float(i['bid'])/len(cotacao)
#VALOR DOS ÚLTIMOS 3 MESES
    def bitcoin1(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/BTC-BRL/90')
        cotacao = requisicao.json()
        self.b3=0
        for i in cotacao:
            self.b3 = (self.b3+float(i['bid']))/len(cotacao)
#VALOR DOS ÚLTIMOS 3 MESES
    def ethereum1(self):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/ETH-BRL/90')
        cotacao = requisicao.json()
        self.et3=0
        for i in cotacao:
            self.et3 = (self.et3+float(i['bid']))/len(cotacao)

#VALOR VARIÁVEL, ESCOLHA DO CLIENTE
    def dolar2(self, meses):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/USD-BRL/{meses*30}')
        cotacao = requisicao.json()
        self.md=0
        for i in cotacao:
            self.md = (self.md+float(i['bid']))/len(cotacao)
#VALOR VARIÁVEL, ESCOLHA DO CLIENTE  
    def euro2(self, meses):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/EUR-BRL/{meses*30}')
        cotacao = requisicao.json()
        self.me=0
        for i in cotacao:
            self.me = (self.me+float(i['bid']))//len(cotacao)
#VALOR VARIÁVEL, ESCOLHA DO CLIENTE
    def libra2(self, meses):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/GBP-BRL/{meses*30}')
        cotacao = requisicao.json()
        self.ml=0
        for i in cotacao:
            self.ml = (self.ml+float(i['bid']))/len(cotacao)
#VALOR VARIÁVEL, ESCOLHA DO CLIENTE
    def bitcoin2(self, meses):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/BTC-BRL/{meses*30}')
        cotacao = requisicao.json()
        self.mb=0
        for i in cotacao:
            self.mb = (self.mb+float(i['bid']))//len(cotacao)
#VALOR VARIÁVEL, ESCOLHA DO CLIENTE
    def ethereum2(self, meses):
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/ETH-BRL/{meses*30}')
        cotacao = requisicao.json()
        self.met=0
        for i in cotacao:
            self.met = (self.met+float(i['bid']))/len(cotacao)
