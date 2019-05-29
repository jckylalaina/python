from tkinter import *
 
def deplacement():
    global dx, dy 
    if (canvas.coords(balle1)[1]<0):
        dy=-1*dy
    if (canvas.coords(balle1)[0]<0) or (canvas.coords(balle1)[2]>500):
        dx=-1*dx
    if canvas.coords(balle1)[3]>canvas.coords(raquette)[1] and \
    canvas.coords(balle1)[0]<canvas.coords(raquette)[2] and \
    canvas.coords(balle1)[2]>canvas.coords(raquette)[0]:
    	dy=-1*dy
    
    canvas.move(balle1,dx,dy)
    #On repete cette fonction
    tk.after(15,deplacement)
 
#Deplacement de la balle au départ:
dy = 8
dx = 5
 
def droite(event):
	canvas.move(raquette,10,0)

def gauche(event):
	canvas.move(raquette,-10,0)	
#On cree une fenetre et un canevas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)
 
#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()
 
#On cree une balle:
balle1 = canvas.create_oval(10,10,30,30,fill='blue')
raquette = canvas.create_rectangle(200,380,300,390,fill='red')
 
deplacement()
 

canvas.bind_all('<Right>',droite)
canvas.bind_all('<Left>',gauche)
#On lance la boucle principale:
tk.mainloop()