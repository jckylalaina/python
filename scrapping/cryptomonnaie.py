import os
import csv
import json
import requests
import time
from bs4 import BeautifulSoup

a = time.time()
#entrée dans l'url  coinmarket
crypto = requests.get("https://coinmarketcap.com/all/views/all/")
crypto = crypto.content
soup = BeautifulSoup(crypto)
#prend la balise td avec la class text-left ;l abbreviation des crypto
crypto_abbr = soup.find_all("td", {"class": "text-left col-symbol"})
#prend le prix de tou les crypto
crypto_price = soup.find_all("a",{"class":"price"})
#convertit lesy balise en txt
liste_titre = [elt.string.strip() for elt in crypto_abbr]
price = [elt.string.strip() for elt in crypto_price]
#nouveau hash ou dictioonaire
tab = {}
#associ chaque crypto avec son prix
for i in range(0,len(crypto_abbr)):
	tab[liste_titre[i]] = price[i]
print(tab)

#ouvre ou cree un fichier csv avec permission d'ecrire
with open("scraping_crypto.csv", "w", encoding="utf-8") as fichier:
	writer = csv.writer(fichier)
	#pour chaque cle et valeur on ecri dans le fichier
	for keys,value in tab.items():

		writer.writerow((keys,value))

#ouverture ou creation dans fichier json avec permission d'ecrire
with open('scrapping_crypto.json','w') as f:
	#enregistre le dico tab dans le fichier json
	f.write(json.dumps(tab,indent=4))

b = time.time() - a
print(b)  

