from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import SQLManager
import subprocess

def recup_add_data():
    print("Ajout des données dans la table SQL")

def OnSelectList():
    print("OnSelectList")

add_sequence = Tk()
add_sequence.title("Module de création de séquences")
# window.geometry("1080x720")
add_sequence.minsize(1080,720)
add_sequence.maxsize(1080,720)
add_sequence.iconbitmap("pictures/likeBlack.ico")
add_sequence.config(background='#FFFFFF')

Titre_ajouter = Label(add_sequence, text="Ajout d'une nouvelle séquence", font=("Helvetica", 14), bg="white", fg="black");
Titre_ajouter.pack()

items_frame = Frame(add_sequence, bg="#FFFFFF", border=1)
items_frame.pack()


left_frame_t = Frame(items_frame, border=1)

left_frame_text_side_grid=Frame(left_frame_t)
left_frame_text_side = Label(left_frame_text_side_grid, text="Côté (g ou d) :", font=("Helvetica", 14), fg="black");
left_frame_text_side.pack()
left_frame_text_side_grid.grid(row=0, column=0)

left_frame_value_side_grid=Frame(left_frame_t)
left_frame_value_side = Entry(left_frame_value_side_grid, width=3)
left_frame_value_side.pack()
left_frame_value_side_grid.grid(row=0, column=1)

left_frame_text_color_grid=Frame(left_frame_t)
left_frame_text_color = Label(left_frame_text_color_grid, text="Couleur (j,b,m ou n) :", font=("Helvetica", 14), fg="black");
left_frame_text_color.pack()
left_frame_text_color_grid.grid(row=0, column=2)

left_frame_value_color_grid=Frame(left_frame_t)
left_frame_value_color = Entry(left_frame_value_color_grid, width=3)
left_frame_value_color.pack()
left_frame_value_color_grid.grid(row=0, column=3)

list_of_vid_frame = Frame(left_frame_t, bg="#FFF0F0", border=2)

scrollbar = Scrollbar(list_of_vid_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listeVideos = Listbox(list_of_vid_frame)
listeVideos.configure(width=90,height=35)
listeVideos.bind('<<ListboxSelect>>', OnSelectList)

my_list=SQLManager.tri_and_title("d","b")
print("Ma liste dans VM "+str(my_list))
for item in my_list:
    label_in_list=str(item[0])+" : >"+item[1]+"< Coté : >"+item[2]+"< Couleur : >"+item[3]+"< Longueur : >"+str(item[4])+"< Fichier : >"+item[5]+"< Date : >"+str(item[6])
    listeVideos.insert(item[0],label_in_list)

# attach listbox to scrollbar
listeVideos.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listeVideos.yview)
list_of_vid_frame.grid(row=1, column=0,columnspan=4)
listeVideos.pack()

left_frame_t.grid(row=0, column=0)



right_frame_t = Frame(items_frame, border=1)

right_frame_text_title_grid=Frame(right_frame_t)
right_frame_text_title = Label(right_frame_text_title_grid, text="Titre : ", font=("Helvetica", 14), fg="black");
right_frame_text_title.pack()
right_frame_text_title_grid.grid(row=0, column=0)

right_frame_value_title_grid=Frame(right_frame_t)
right_frame_value_title = Entry(right_frame_value_title_grid, width=30)
right_frame_value_title.pack()
right_frame_value_title_grid.grid(row=0, column=1)

right_frame_t.grid(row=0, column=1)



spacer = Label(add_sequence, text="", font=("Helvetica", 10), fg="black");
spacer.pack()

buttons_frame=Frame(add_sequence,border=1)
button_val_t=Frame(buttons_frame,padx=20)
button_val = Button(button_val_t, text="Valider", command=recup_add_data)
button_val.pack()
button_val_t.grid(row=0,column=0)

button_test_t=Frame(buttons_frame,padx=20)
button_test= Button(button_test_t, text="Test")
button_test.pack()
button_test_t.grid(row=0,column=1)

button_dismiss_t=Frame(buttons_frame,padx=20)
button_dismiss = Button(button_dismiss_t, text="Annuler", command=add_sequence.destroy)
button_dismiss.pack()
button_dismiss_t.grid(row=0,column=2)

buttons_frame.pack()

add_sequence.mainloop()