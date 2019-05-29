
from tkinter import *

def Clic(event):
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    # on dessine un carré
    r = 5
    Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline="black",fill="green")

def Effacer():
    Canevas.delete(ALL)

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Souris")

# Création d'un widget Canvas
Largeur = 480
Hauteur = 320
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ="white")
# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur Clic()
Canevas.bind("<Button-1>", Clic)
Canevas.pack(padx =5, pady =5)

# Création d'un widget Button (bouton Effacer)
Button(Mafenetre, text ="Effacer", command = Effacer).pack(side=LEFT,padx = 5,pady = 5)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text ="Quitter", command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

Mafenetre.mainloop()