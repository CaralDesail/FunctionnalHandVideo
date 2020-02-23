from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import SQLManager


def recup_mod_data(): # function that will use tkinter input to feed SQL database trougth SQLManager after check
    name = name_frame_value.get()
    side = side_frame_value.get()
    color = color_frame_value.get()
    length= length_frame_value.get()
    filename = filename_frame_value.get()


    if (name !="" and side !="" and color !="" and length!="" and filename!=""): #if all fields are fullfield
        test_passed=True
    else :
        test_passed=False

    if test_passed : #if all fields are fullfield
        print("Pas de résultats équivalent, enregistrement ok ")
        SQLManager.delete_vid(indexSel)
        SQLManager.ajout_dyn(name, side, color, length, filename)
        messagebox.showinfo("Validation", "Enregistrement ok")
        mod_video.quit()

    else :
        print("Remplir tous les champs SVP")
        


#define the value of indexSel
try: # if it is ok, that is to say sys.argv has return someting valid, indexSel takes the number
    indexSel=int(sys.argv[1])
    print("argument passé :", indexSel)
except IndexError: # if exception
    indexSel=99
    print("appel direct du script donc index par défaut à ",indexSel)


mod_video = Tk()
mod_video.title("Modification d'une vidéo")
# window.geometry("1080x720")
mod_video.minsize(800, 300)
mod_video.iconbitmap("pictures/likeBlack.ico")
mod_video.config(background='#FFFFFF')

Titre_ajouter = Label(mod_video, text="Ajouter", font=("Helvetica", 14), bg="white", fg="black");
Titre_ajouter.pack()

items_frame = Frame(mod_video, bg="#FFFFFF", border=1)
items_frame.pack()

name_frame_t = Frame(items_frame, border=1)
name_frame_text = Label(name_frame_t, text="Nom", font=("Helvetica", 14), fg="black");
name_frame_text.pack()
name_frame_value = Entry(name_frame_t, width=30)
name_frame_value.pack()
name_frame_t.grid(row=0, column=0)

side_frame_t = Frame(items_frame, border=1)
side_frame_text = Label(side_frame_t, text="Côté (g ou d)", font=("Helvetica", 14), fg="black");
side_frame_text.pack()
side_frame_value = Entry(side_frame_t)
side_frame_value.pack()
side_frame_t.grid(row=0, column=1)

color_frame_t = Frame(items_frame, border=1)
color_frame_text = Label(color_frame_t, text="Couleur (j,b,m,n)", font=("Helvetica", 14), fg="black");
color_frame_text.pack()
color_frame_value = Entry(color_frame_t)
color_frame_value.pack()
color_frame_t.grid(row=0, column=2)

length_frame_t = Frame(items_frame, border=1)
length_frame_text = Label(length_frame_t, text="Durée(en s)", font=("Helvetica", 14), fg="black");
length_frame_text.pack()
length_frame_value = Entry(length_frame_t)
length_frame_value.pack()
length_frame_t.grid(row=0, column=3)

filename_frame_t = Frame(items_frame, border=1)
filename_frame_text = Label(filename_frame_t, text="Fichier", font=("Helvetica", 14), fg="black");
filename_frame_text.pack()
filename_frame_value = Entry(filename_frame_t, width=30)
filename_frame_value.pack()
filename_frame_t.grid(row=0, column=4)

button_val = Button(mod_video, text="Valider", command=recup_mod_data)
button_val.pack()

spacer = Label(mod_video, text="", font=("Helvetica", 10), fg="black");
spacer.pack()
button_dismiss = Button(mod_video, text="Annuler", command=mod_video.destroy)
button_dismiss.pack()

#will fill the different fields with values
chain_to_use=SQLManager.find_vid_by_id(indexSel)
name_frame_value.insert(0,chain_to_use[0][1])
side_frame_value.insert(0,chain_to_use[0][2])
color_frame_value.insert(0,chain_to_use[0][3])
length_frame_value.insert(0,chain_to_use[0][4])
filename_frame_value.insert(0,chain_to_use[0][5])

mod_video.mainloop()

