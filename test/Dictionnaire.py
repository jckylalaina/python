# -*- coding: utf-8 -*-

# class Personne():
    
#     "" """Classe définissant une personne.
    
#     Elle possède comme attributs :
#     nom -- le nom de la personne
#     prenom -- son prénom
#     age -- son âge
#     lieu_residence -- son lieu de résidence
    
#     Le nom et le prénom doivent être passés au constructeur."""
    
#     def __new__(cls, nom, prenom):
#         print("Appel de la méthode __new__ de la classe {}".format(cls))
#         # On laisse le travail à object
#         return object.__new__(cls, nom, prenom)
    
#     def __init__(self, nom, prenom):
#         "" """Constructeur de notre personne."""
#         print("Appel de la méthode __init__")
#         self.nom = nom
#         self.prenom = prenom
#         self.age = 23
#         self.lieu_residence = "Lyon"

# jacky = Personne("jacky","Doe")
# print(jacky.nom)



def nouveau(cls,nom,prenom):
	return object.__new__recent(cls,nom,prenom)

def init(user,nom,prenom):
	user.nom = nom
	user.prenom = prenom

def presenter(user):
	return "vous etes {} {}".format(user.nom,user.prenom)

methode = {
	"__new__" : nouveau,
	"__init__" : init,
	"__repr__" : presenter
}				

User = type("User",(),methode)


a = User("jacky","lalaina")
print(a.nom)