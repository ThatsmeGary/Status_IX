import requests
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore
from prettytable import PrettyTable




link = requests.get(url='https://status.ix.br/').content
html = BeautifulSoup(link,'html.parser')

sites = []

ESTADO = input(str("DIGITE A SIGLA DO ESTADO QUE VOCÊ DESEJAR VER O STATUS DE TRÁFEGO ==>  "))

for indicie, data in enumerate(html.find_all("li")):
    SIGLA = data.get_text(separator=' ', strip=True)
    sites.append([SIGLA])


header = PrettyTable([Fore.LIGHTYELLOW_EX + f"Recuperando informações de {ESTADO}..." + Fore.RESET])

sleep(2)
for i, x in enumerate(sites):
    for y in x:
        if f'{ESTADO}' in y:
            if i == 0:
                pass
    
            elif "Indisponibilidade parcial" in y:
                header.add_row([Fore.RED + y + Fore.RESET])
            else:        
                header.add_row([Fore.GREEN + y+ Fore.RESET])
        else:
            pass
print(header)