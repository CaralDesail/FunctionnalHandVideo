import MovieManager
from tkinter import *
from tkinter import messagebox, filedialog
import SQLManager
import subprocess
from moviepy.video.io.VideoFileClip import VideoFileClip


def Main_VideoManagement_Window():
    index_selected = 9999  # is the index of selected video (sql index, not listbox index that are differents ...


    def OnSelectList(event):
        print("changement de liste" + str(event))
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected "%s"' % (value))
        expr_reg = r"^[0-9]{1,5}"

        global index_selected
        index_selected = re.findall(expr_reg, value)[
            0]  # will find the corresponding index with regular expression (THERE IS A MOST SIMPLE WAY TO DO IT but I didn't succeded)
        print(index_selected)

    def mod_video():
        global index_selected
        MOD_VM_window(index_selected)

    def del_video():
        global index_selected
        SQLManager.delete_vid(index_selected)
        my_list = SQLManager.readAll()
        print("Ma liste dans VM " + str(my_list))
        listeVideos.delete(0, END)
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
        item = SQLManager.find_vid_by_id(index_selected)
        MovieManager.video_launch(item[0][5])

    def ADD_VM_Window(): #all the container of add video frame

        def find_file_to_add():
            file_selected = filedialog.askopenfilename(title="Selectionnez le fichier",
                                                       filetypes=(("mpeg files", "*.mp4"), ("all files", "*.*")))
            # dialogue box where user will select the file to add
            print("Find the file : ", file_selected)  # catch the entire line
            liste_of_filepath = file_selected.split("/")  # catch the name of file
            filename = liste_of_filepath[-1]  # take it
            filename_frame_value.delete(0, END)
            filename_frame_value.insert(0, filename)  # and fulfill the field

            length_frame_value.delete(0, END)  # ... the same for duration
            clip = VideoFileClip(file_selected)  # using VideoFileClip that is to say moviepy (on pygame)
            clip_length = clip.duration
            clip.close()  # close the file reading to avoid exception.
            length_frame_value.insert(0, clip_length)

        def recup_add_data():  # function that will use tkinter input to feed SQL database trougth SQLManager after check
            name = name_frame_value.get()
            side = side_frame_value.get()
            color = color_frame_value.get()
            length = length_frame_value.get()
            filename = filename_frame_value.get()

            if (
                    name != "" and side != "" and color != "" and length != "" and filename != ""):  # if all fields are fullfield
                test_passed = True
            else:
                test_passed = False

            if test_passed:  # if all fields are fullfield
                # then no_previous record check :
                if (SQLManager.retrive_video_path(name, side, color) == []):
                    print("Pas de résultats équivalent, enregistrement ok ")
                    SQLManager.ajout_dyn(name, side, color, length, filename)
                    messagebox.showinfo("Validation", "Enregistrement ok")
                    ref_video()
                    add_video.destroy()

                else:
                    print("Un enregistrement existe déjà avec les mêmes références coleur, côté et action")
                    print(SQLManager.retrive_video_path(name, side, color))
            else:
                print("Remplir tous les champs SVP")

        add_video = Toplevel()
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

    def MOD_VM_window(indexSelPasse):

        indexSel=indexSelPasse

        def recup_mod_data():  # function that will use tkinter input to feed SQL database trougth SQLManager after check
            name = name_frame_value.get()
            side = side_frame_value.get()
            color = color_frame_value.get()
            length = length_frame_value.get()
            filename = filename_frame_value.get()

            if (
                    name != "" and side != "" and color != "" and length != "" and filename != ""):  # if all fields are fullfield
                test_passed = True
            else:
                test_passed = False

            if test_passed:  # if all fields are fullfield
                print("Pas de résultats équivalent, enregistrement ok ")
                SQLManager.delete_vid(indexSel)
                SQLManager.ajout_dyn(name, side, color, length, filename)
                messagebox.showinfo("Validation", "Enregistrement ok")
                mod_video.destroy()

            else:
                print("Remplir tous les champs SVP")



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

        # will fill the different fields with values
        chain_to_use = SQLManager.find_vid_by_id(indexSel)
        name_frame_value.insert(0, chain_to_use[0][1])
        side_frame_value.insert(0, chain_to_use[0][2])
        color_frame_value.insert(0, chain_to_use[0][3])
        length_frame_value.insert(0, chain_to_use[0][4])
        filename_frame_value.insert(0, chain_to_use[0][5])

        mod_video.mainloop()

    windowVM = Tk()


    windowVM.title("Gestion des videos")
    # window.geometry("1080x720")
    windowVM.minsize(900, 700)
    windowVM.maxsize(900, 700)
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
    add_button = Button(add_button_frame, text="Ajouter", border=1,font=("Helvetica", 12),command=ADD_VM_Window);
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

