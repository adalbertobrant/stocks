import json
import assets_mon as ats
import pandas as pd
import datetime as dt
from datetime import date
from rich.console import Console
from rich.table import Table
import os


json_list = []

# clear screen
def clear():
  return os.system('cls' if os.name == 'nt' else 'clear')



# data from user

def input_stock(stock):
  clear()
  try:
    x = ats.Stock(stock)
  except AssertionError as e:
    if e.args[0]['chart']['error']['code'] == 'Not Found':
        print(f"{x} not found!!")
    else:
        raise
  except AttributeError as e:
    print(e)

  clear()
  return x
#########################################
#def qtd_input(qtd, lista):
#  for i in range(0,qtd):
#    lista.append(input_stock())

#qtd = int(input(f"Entre a quantidade de ações a ser prospectada -> "))
#lista = []
#qtd_input(qtd,lista)
###########################################

# pega uma lista de stocks e retorna o resultado.
lista = []
with open('./models/stocks.txt','r') as stcks:
  stocks = stcks.read().splitlines()

for i in stocks:
  stock = input_stock(i)
  lista.append(stock)

# A-Z order
lista.sort(key=lambda x: x.symbol)

# Tabela.

table = Table(title = "Stocks closing price Tomorrow")
rows = []

weeks = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
close_date = dt.datetime.now()
day = weeks[close_date.weekday()]
if day == 'sábado' or day == 'domingo':
  day = 'segunda'
close_date= close_date.strftime('%d/%m/%Y')
ss = "Stock Symbol"
fcp = f"Future Close Price - {day}"

for i in lista:
  rows.append((i.symbol, str(i.tomorrow)))
  json_list.append({i.symbol:str(i.tomorrow)})

columns = [ss, fcp, ]

for column in columns:
  table.add_column(column)
for row in rows:
  
  table.add_row(*row, style='bright_green')

console = Console()
console.print(table)

# json file
day_today = date.today().strftime("%d-%m-%Y")
with open(f"./json/stocks_json_{day_today}.json","w") as stocks_json:
  json.dump(json_list, stocks_json)

  
