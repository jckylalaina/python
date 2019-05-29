from tkinter import *
 
def move():
    global x
    global y,pX,pY
    global Serpent
    canvas.delete('all')
    i=len(Serpent)-1
    j=0
    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]
        Serpent[i][1]=Serpent[i-1][1]
        canvas.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0] +10, Serpent[i][1]+10,outline='green', fill='black') 
        i=i-1


tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)





move()

#On lance la boucle principale:
tk.mainloop()
