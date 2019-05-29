# -*- coding: utf-8 -*-
class Personne:
    "" """Classe représentant une personne"""

    def __init__(self, nom):
        "" """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"

    def __str__(self):
        "" """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)


class AgentSpecial(Personne):
    "" """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""

    def __init__(self, nom, matricule):
        "" """Un agent se définit par son nom et son matricule"""
        self.nom = nom
        self.matricule = matricule

    def __str__(self):
        "" """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

      # server.quit()
