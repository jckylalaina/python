from tkinter import *
 
def deplacement():
    global dx, dy 
    
    # if canvas.coords(balle1)[3]>canvas.coords(raquette)[1] and \
    # canvas.coords(balle1)[0]<canvas.coords(raquette)[2] and \
    # canvas.coords(balle1)[2]>canvas.coords(raquette)[0]:
    # 	dy=-1*dy
    
    canvas.move(snake,dx,dy)
    #On repete cette fonction
    tk.after(15,deplacement)
 
#Deplacement de la balle au départ:
dy = 0
dx = 0

#On cree une fenetre et un canevas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)
 
#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()
 
#On cree une balle:
tete = canvas.create_oval(8,8,20,20,fill='blue')
body = canvas.create_oval(8,8,18,18,fill='blue')
snake = [tete,body]
 
deplacement()
 


#On lance la boucle principale:
tk.mainloop()