from tkinter import *
from tkinter import ttk
import SQLManager
import re
import subprocess


index_selected=9999 # is the index of selected video (sql index, not listbox index that are differents ...

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


def add_sequence():
    subprocess.call("python SeqM_addsequence.py")

def mod_sequence():
    print("mod video")
    global index_selected
    subprocess.call(['python', 'SeqM_modsequence.py', index_selected])

def del_sequence():
    global index_selected
    SQLManager.delete_seq(index_selected)

def ref_sequence():
    listeSequences.delete(0, END)
    my_list = SQLManager.list_of_sequence()
    print("Ma liste dans SM " + str(my_list))
    for item in my_list:
        label_in_list = str(item[0]) + " : >" + item[1] + "< Couleur : >" + item[2] + "< Coté : >" + item[
            3] + "< Longueur : >" + str(item[4]) + "< Schema : >" + item[5]
        listeSequences.insert(item[0], label_in_list)

windowSM = Tk()

windowSM.title("Gestion des séquences")
# window.geometry("1080x720")
windowSM.minsize(900, 700)
windowSM.iconbitmap("pictures/likeBlack.ico")
windowSM.config(background='#FFFFFF')

top_title = Label(windowSM, text="Gestion des séquences", font=("Helvetica", 14), bg="white", fg="black");
top_title.pack()

list_of_vid_frame = Frame(windowSM, bg="#FFFFFF", border=1)

scrollbar = Scrollbar(list_of_vid_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listeSequences = Listbox(list_of_vid_frame)
listeSequences.configure(width=140, height=35)
listeSequences.bind('<<ListboxSelect>>', OnSelectList)

my_list=SQLManager.list_of_sequence()
print("Ma liste dans SM "+str(my_list))
for item in my_list:
    label_in_list=str(item[0])+" : >"+item[1]+"< Couleur : >"+item[2]+"< Coté : >"+item[3]+"< Longueur : >"+str(item[4])+"< Schema : >"+item[5]
    listeSequences.insert(item[0], label_in_list)

# attach listbox to scrollbar
listeSequences.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listeSequences.yview)

buttons_frame = Frame(windowSM, bg="#FFFFFF", border=1)

add_button_frame=Frame(buttons_frame,padx=20)
add_button = Button(add_button_frame, text="Nouvelle séquence", border=1,font=("Helvetica", 12),bg="#2ECC71",command=add_sequence);
add_button_frame.grid(row=0, column=0)
add_button.pack()

modify_button_frame=Frame(buttons_frame,padx=20)
modify_button = Button(modify_button_frame, text="Modifier", border=1,font=("Helvetica", 12),bg="#EBEBEB",command=mod_sequence);
modify_button_frame.grid(row=0, column=1)
modify_button.pack()

delete_button_frame=Frame(buttons_frame,padx=20)
delete_button = Button(delete_button_frame, text="Supprimer", border=1,font=("Helvetica", 12),bg="#922B21",command=del_sequence);
delete_button_frame.grid(row=0, column=2)
delete_button.pack()

refresh_button_frame=Frame(buttons_frame,padx=20)
refresh_button = Button(refresh_button_frame, text="Actualiser", border=1,font=("Helvetica", 12),bg="#F4D03F",command=ref_sequence);
refresh_button_frame.grid(row=0, column=3)
refresh_button.pack()

list_of_vid_frame.pack()
buttons_frame.pack()
listeSequences.pack()

windowSM.mainloop()