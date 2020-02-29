from tkinter import *


def secondaire():
    toplevel = Toplevel()
    label = Label(toplevel, text='coucou')
    label.pack()



fenetre = Tk()  ##

bouton = Button(fenetre, text='Secondaire', command=secondaire)
bouton.pack()

fenetre.mainloop()  ## La seule boucle.