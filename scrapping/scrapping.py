import os
import csv
import requests
from bs4 import BeautifulSoup

Paris = requests.get("https://www.annuaire-des-mairies.com/paris.html")
Paris = Paris.content
soup = BeautifulSoup(Paris)
arrondissement = soup.find_all("a", {"class": "lientxt"})
liste_titre = [elt.string.strip() for elt in arrondissement]
print(liste_titre)

with open("donnees.csv", "w", encoding="utf-8") as fichier:
    for elt in liste_titre:
        elt = elt.split(" ")
        elt = "-".join(elt)
        ville = requests.get(
            "https://www.annuaire-des-mairies.com/75/{}.html".format(elt.lower())
        )
        ville = ville.content
        soup = BeautifulSoup(ville).body
        email = soup.div.table.tbody.find_all("tr")[3].find_all("td")[1]
        print(elt, email.string.strip(), sep=" -> ")

        writer = csv.writer(fichier)
        writer.writerow((elt, email.string.strip()))

os.system("black scrapping.py")
