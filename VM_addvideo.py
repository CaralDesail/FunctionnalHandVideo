from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import SQLManager
import subprocess
from moviepy.editor import VideoFileClip

def find_file_to_add():
    file_selected=filedialog.askopenfilename(title = "Selecttionnez le fichier",filetypes = (("mpeg files","*.mp4"),("all files","*.*")))
    # dialogue box where user will select the file to add
    print("Find the file : ",file_selected) #catch the entire line
    liste_of_filepath=file_selected.split("/") #catch the name of file
    filename=liste_of_filepath[-1] #take it
    filename_frame_value.delete(0, END)
    filename_frame_value.insert(0, filename) #and fulfill the field

    length_frame_value.delete(0,END)#... the same for duration
    clip = VideoFileClip(file_selected)  # using VideoFileClip that is to say moviepy (on pygame)
    clip_length=clip.duration
    clip.close() # close the file reading to avoid exception.
    length_frame_value.insert(0, clip_length)



def recup_add_data(): # function that will use tkinter input to feed SQL database trougth SQLManager after check
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
        # then no_previous record check :
        if (SQLManager.retrive_video_path(name,side,color)==[]):
            print("Pas de résultats équivalent, enregistrement ok ")
            SQLManager.ajout_dyn(name, side, color, length, filename)
            messagebox.showinfo("Validation", "Enregistrement ok")

            add_video.quit()

        else :
            print("Un enregistrement existe déjà avec les mêmes références coleur, côté et action")
            print(SQLManager.retrive_video_path(name, side, color))
    else :
        print("Remplir tous les champs SVP")


add_video = Tk()
add_video.title("Ajout d'une vidéo")
# window.geometry("1080x720")
add_video.minsize(800, 300)
add_video.maxsize(800, 300)
add_video.iconbitmap("pictures/likeBlack.ico")
add_video.config(background='#FFFFFF')

Titre_ajouter = Label(add_video, text="Ajouter", font=("Helvetica", 14), bg="white", fg="black");
Titre_ajouter.pack()

items_frame = Frame(add_video, bg="#FFFFFF", border=1)
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

spacer = Label(add_video, text="", font=("Helvetica", 10), fg="black");
spacer.pack()

button_find_video = Button(add_video, text="Chercher le fichier", command=find_file_to_add)
button_find_video.pack()

spacer = Label(add_video, text="", font=("Helvetica", 10), fg="black");
spacer.pack()

button_val = Button(add_video, text="Valider", command=recup_add_data)
button_val.pack()

spacer = Label(add_video, text="", font=("Helvetica", 10), fg="black");
spacer.pack()

button_dismiss = Button(add_video, text="Annuler", command=add_video.destroy)
button_dismiss.pack()

add_video.mainloop()