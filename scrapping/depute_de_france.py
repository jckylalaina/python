import os
import csv
import json
import requests
import time
from bs4 import BeautifulSoup

dic = {}
i = 0
while i<=570:
	site_depute = requests.get("https://www.voxpublic.org/spip.php?page=annuaire&cat=deputes&debut_deputes={}#pagination_deputes".format(str(i)))
	site = site_depute.content
	soup = BeautifulSoup(site)
	
	result = soup.find_all('ul',{'class':'no_puce list_ann'})
	for elt in result:
		titre = elt.h2.string.strip()
		li = elt.find_all("li")
		split = elt.get_text().split("\n")
		n = split[2:-1]
		tab = []
		for i in n:
			a = i.split(":")
			tab.append(a[-1])
		dic[titre] = {"Circonscription":tab[1],
		"Groupe_politique":tab[2],
		"fonction":tab[3],
		"email":tab[4],
		}
		print(dic)
	i = int(i)
	i+=10	
	
	