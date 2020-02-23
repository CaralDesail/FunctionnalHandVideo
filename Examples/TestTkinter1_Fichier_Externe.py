from tkinter import *
from random import randint,choice
import string

def generate_text():
    chain_min=6
    chain_max=12
    all_chars=string.ascii_letters+string.punctuation+string.digits
    chain_to_print= "".join(choice(all_chars) for x in range(randint(chain_min, chain_max)))
    field_entry.delete(0,END)
    field_entry.insert(0,chain_to_print)


#creer fenetre

window=Tk()
window.title("Fenetre exterieure")
window.minsize(720,480)
window.config(background="#4065A4")

#creer frame principale
frame=Frame(window, bg="#4065A4")
#https://www.flaticon.com/
#creation d'image
widthI=300
heightI=500
image=PhotoImage(file="../pictures/hand.png").zoom(35).subsample(32)
canvas=Canvas(frame,width=widthI,height=heightI, bg="#4065A4", bd=0, highlightthickness=0 )
canvas.create_image(widthI/2,heightI/2,image=image)
canvas.grid(row=0, column=0)

#creer une sous boite
right_frame=Frame(frame,bg="#4065A4")
right_frame.grid(row=0, column=1)

#créer titre ecrit
label_title=Label(right_frame, text="Mon texte", font=("Helvetica",20), bg="#4065A4", fg="black");
label_title.pack()
#créer champ
field_entry=Entry(right_frame, font=("Helvetica",10), bg="#4065A4", fg="black");
field_entry.pack()
#créer boutton
my_button=Button(right_frame, text="le boutton",font=("Helvetica",10), bg="#4065A4", fg="black", command=generate_text);
my_button.pack(fill=X)


#afficher la frame
frame.pack(expand=YES)



#creation barre de menus
menu_bar=Menu(window)
#creer premier menu
file_menu= Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_text)
file_menu.add_command(label="Quitter",command = window.quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configurer la fenetre pour ajouter la menu bar
window.config(menu=menu_bar)

window.mainloop()