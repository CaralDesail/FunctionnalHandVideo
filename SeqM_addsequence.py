from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import SQLManager
import SeqMClass

liste_dynamique=SeqMClass.MySequence()

def recup_add_data():
    print("Ajout des données dans la table SQL")

def add_video():
    video=SQLManager.find_vid_by_id(index_selected)
    liste_dynamique.addToList(video)

    RefreshChosenList(liste_dynamique.return_list())

def del_video():
    liste_dynamique.deleteFromList(chosen_index_selected)
    RefreshChosenList(liste_dynamique.return_list())

def up_video():
    liste_dynamique.up(chosen_index_selected)
    RefreshChosenList(liste_dynamique.return_list())


def down_video():
    liste_dynamique.down(chosen_index_selected)
    RefreshChosenList(liste_dynamique.return_list())

def OnSelectList(event):
    print("changement de liste"+str(event))
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected "%s"' % (value))
    expr_reg=r"^[0-9]{1,5}"

    global index_selected
    index_selected=re.findall(expr_reg,value)[0] #will find the corresponding index with regular expression (THERE IS A MOST SIMPLE WAY TO DO IT but I didn't succeded)
    print(index_selected)

def SideAndColorChoseEvent(event): # when changes in color and side entry box, will recalculate what to show in video selection listbox
    side=left_frame_value_side.get()
    color=left_frame_value_color.get()

    print("Le côté est :",side, " et la couleur ",color)
    listeVideos.delete(0,END)
    list_to_show=SQLManager.tri_and_title(side,color)
    print(list_to_show)
    for item in list_to_show:
        label_in_list = str(item[0])+" : "+str(item[1]) +" : Longueur : " + str(item[4])
        listeVideos.insert(item[0], label_in_list)

def OnSelectChosenList(event):
    print("changement de liste"+str(event))
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected ', value, ' a l index ', index)
    global chosen_index_selected
    chosen_index_selected = index

def RefreshChosenList(my_list):
    print(my_list)
    index=0
    listeChosenVideos.delete(0,END)
    for item in my_list:
        index+=1
        listeChosenVideos.insert(index, item)


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
left_frame_value_side.bind('<FocusOut>',SideAndColorChoseEvent)
left_frame_value_side.bind('<Return>',SideAndColorChoseEvent)
left_frame_value_side_grid.grid(row=0, column=1)

left_frame_text_color_grid=Frame(left_frame_t)
left_frame_text_color = Label(left_frame_text_color_grid, text="Couleur (j,b,m ou n) :", font=("Helvetica", 14), fg="black");
left_frame_text_color.pack()
left_frame_text_color_grid.grid(row=0, column=2)

left_frame_value_color_grid=Frame(left_frame_t)
left_frame_value_color = Entry(left_frame_value_color_grid, width=3)
left_frame_value_color.pack()
left_frame_value_color.bind('<FocusOut>',SideAndColorChoseEvent)
left_frame_value_color.bind('<Return>',SideAndColorChoseEvent)
left_frame_value_color_grid.grid(row=0, column=3)

list_of_vid_frame = Frame(left_frame_t, bg="#FFF0F0", border=2)

scrollbar = Scrollbar(list_of_vid_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listeVideos = Listbox(list_of_vid_frame)
listeVideos.configure(width=90,height=35)
listeVideos.bind('<<ListboxSelect>>', OnSelectList)

my_list=SQLManager.readAll()
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


center_frame = Frame(items_frame, border=1)

button_add = Button(center_frame, text="+", command=add_video)
button_add.pack()
button_del = Button(center_frame, text="- ", command=del_video)
button_del.pack()
button_up = Button(center_frame, text="^", command=up_video)
button_up.pack()
button_down = Button(center_frame, text="v", command=down_video)
button_down.pack()
center_frame.grid(row=0, column=1)


right_frame_t = Frame(items_frame, border=1)

right_frame_text_title_grid=Frame(right_frame_t)
right_frame_text_title = Label(right_frame_text_title_grid, text="Titre : ", font=("Helvetica", 14), fg="black");
right_frame_text_title.pack()
right_frame_text_title_grid.grid(row=0, column=0)

right_frame_value_title_grid=Frame(right_frame_t)
right_frame_value_title = Entry(right_frame_value_title_grid, width=30)
right_frame_value_title.pack()
right_frame_value_title_grid.grid(row=0, column=1)

list_of_selected_vids_grid=Frame(right_frame_t)

list_of_chosen_vid_frame = Frame(list_of_selected_vids_grid, bg="#FFF0F0", border=2)

scrollbar_chosen_list = Scrollbar(list_of_chosen_vid_frame)
scrollbar_chosen_list.pack(side=RIGHT, fill=Y)

listeChosenVideos = Listbox(list_of_chosen_vid_frame)
listeChosenVideos.configure(width=60, height=35)
listeChosenVideos.bind('<<ListboxSelect>>', OnSelectChosenList)

my_list=[[1,"Vide"]]
for item in my_list:
    label_in_list=str(item[0])+" : >"+item[1]
    listeChosenVideos.insert(item[0], label_in_list)

# attach listbox to scrollbar
listeChosenVideos.config(yscrollcommand=scrollbar_chosen_list.set)
scrollbar_chosen_list.config(command=listeChosenVideos.yview)
list_of_chosen_vid_frame.grid(row=1, column=0, columnspan=4)
listeChosenVideos.pack()

list_of_selected_vids_grid.grid(row=1,column=0,columnspan=2)

right_frame_t.grid(row=0, column=2)



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