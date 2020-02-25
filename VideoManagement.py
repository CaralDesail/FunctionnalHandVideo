from tkinter import *
from tkinter import ttk
import SQLManager
import re
import subprocess
import MovieManager


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


def add_video():
    subprocess.call("python VM_addvideo.py")

def mod_video():
    print("mod video")
    global index_selected
    subprocess.call(['python', 'VM_modvideo.py', index_selected])

def del_video():
    global index_selected
    SQLManager.delete_vid(index_selected)
    my_list = SQLManager.readAll()
    print("Ma liste dans VM " + str(my_list))
    listeVideos.delete(0,END)
    for item in my_list:
        label_in_list = str(item[0]) + " : >" + item[1] + "< Coté : >" + item[2] + "< Couleur : >" + item[
            3] + "< Longueur : >" + str(item[4]) + "< Fichier : >" + item[5] + "< Date : >" + str(item[6])
        listeVideos.insert(item[0], label_in_list)

def ref_video():
    listeVideos.delete(0, END)
    my_list = SQLManager.readAll()
    for item in my_list:
        label_in_list = str(item[0]) + " : >" + item[1] + "< Coté : >" + item[2] + "< Couleur : >" + item[
            3] + "< Longueur : >" + str(item[4]) + "< Fichier : >" + item[5] + "< Date : >" + str(item[6])
        listeVideos.insert(item[0], label_in_list)

def play_video():
    global index_selected
    item=SQLManager.find_vid_by_id(index_selected)
    MovieManager.video_launch(item[0][5])

windowVM = Tk()

windowVM.title("Gestion des videos")
# window.geometry("1080x720")
windowVM.minsize(900, 700)
windowVM.iconbitmap("pictures/likeBlack.ico")
windowVM.config(background='#FFFFFF')

top_title = Label(windowVM, text="Gestion des videos",font=("Helvetica", 14), bg="white", fg="black");
top_title.pack()

list_of_vid_frame = Frame(windowVM, bg="#FFFFFF", border=1)

scrollbar = Scrollbar(list_of_vid_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listeVideos = Listbox(list_of_vid_frame)
listeVideos.configure(width=140,height=35)
listeVideos.bind('<<ListboxSelect>>', OnSelectList)

my_list=SQLManager.readAll()
print("Ma liste dans VM "+str(my_list))
for item in my_list:
    label_in_list=str(item[0])+" : >"+item[1]+"< Coté : >"+item[2]+"< Couleur : >"+item[3]+"< Longueur : >"+str(item[4])+"< Fichier : >"+item[5]+"< Date : >"+str(item[6])
    listeVideos.insert(item[0],label_in_list)

# attach listbox to scrollbar
listeVideos.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listeVideos.yview)

buttons_frame = Frame(windowVM, bg="#FFFFFF", border=1)

add_button_frame=Frame(buttons_frame,padx=20)
add_button = Button(add_button_frame, text="Ajouter", border=1,font=("Helvetica", 12),command=add_video);
add_button_frame.grid(row=0, column=0)
add_button.pack()

modify_button_frame=Frame(buttons_frame,padx=20)
modify_button = Button(modify_button_frame, text="Modifier", border=1,font=("Helvetica", 12),command=mod_video);
modify_button_frame.grid(row=0, column=1)
modify_button.pack()

delete_button_frame=Frame(buttons_frame,padx=20)
delete_button = Button(delete_button_frame, text="Supprimer", border=1,font=("Helvetica", 12),command=del_video);
delete_button_frame.grid(row=0, column=2)
delete_button.pack()

refresh_button_frame=Frame(buttons_frame,padx=20)
refresh_button = Button(refresh_button_frame, text="Actualiser", border=1,font=("Helvetica", 12),command=ref_video);
refresh_button_frame.grid(row=0, column=3)
refresh_button.pack()

play_button_frame=Frame(buttons_frame,padx=20)
play_button = Button(play_button_frame, text="Jouer", border=1,font=("Helvetica", 12),command=play_video);
play_button_frame.grid(row=0, column=4)
play_button.pack()

list_of_vid_frame.pack()
buttons_frame.pack()
listeVideos.pack()




windowVM.mainloop()