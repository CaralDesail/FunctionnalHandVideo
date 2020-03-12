liste_dynamique_mod = SeqMClass.MySequence()  # name of local object


def recup_spec_seq_Id():
    # print("Récupération des infos")
    global index_selected_int
    data_of_seq = SQLManager.spec_from_id(index_selected_int)
    # print("Et importé dans mod_sequence",data_of_seq)
    return data_of_seq


def feed_fields_from_db():
    info_chain = recup_spec_seq_Id()  # call the function that will grab informations of sequences from database
    print("La liste récupérée contient : ", info_chain)
    # feed of different fields:
    right_frame_value_title.insert(0, info_chain[0][1])
    left_frame_value_side.insert(0, info_chain[0][3])
    left_frame_value_color.insert(0, info_chain[0][2])

    # recalculate what to show in left list of videos
    listeVideos.delete(0, END)
    list_to_show = SQLManager.tri_and_title(info_chain[0][3], info_chain[0][2])
    print(list_to_show)
    for item in list_to_show:
        label_in_list = str(item[0]) + " : " + str(item[1]) + " : Longueur : " + str(item[4])
        listeVideos.insert(item[0], label_in_list)


def add_video():
    video = SQLManager.find_vid_by_id(index_selected)
    liste_dynamique_mod.addToList(video)

    newduree = "          Durée : " + str(liste_dynamique_mod.calcul_total_len())
    texte_duree.config(text=newduree)
    RefreshChosenList(liste_dynamique_mod.return_list())


def del_video():
    liste_dynamique_mod.deleteFromList(chosen_index_selected)

    newduree = "          Durée : " + str(liste_dynamique_mod.calcul_total_len())
    texte_duree.config(text=newduree)
    RefreshChosenList(liste_dynamique_mod.return_list())


def up_video():
    liste_dynamique_mod.up(chosen_index_selected)
    RefreshChosenList(liste_dynamique_mod.return_list())


def down_video():
    liste_dynamique_mod.down(chosen_index_selected)
    RefreshChosenList(liste_dynamique_mod.return_list())


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


def SideAndColorChoseEvent(
        event):  # when changes in color and side entry box, will recalculate what to show in video selection listbox
    side = left_frame_value_side.get()
    color = left_frame_value_color.get()

    print("Le côté est :", side, " et la couleur ", color)
    listeVideos.delete(0, END)
    list_to_show = SQLManager.tri_and_title(side, color)
    print(list_to_show)
    for item in list_to_show:
        label_in_list = str(item[0]) + " : " + str(item[1]) + " : Longueur : " + str(item[4])
        listeVideos.insert(item[0], label_in_list)


def OnSelectChosenList(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected ', value, ' a l index ', index)
    global chosen_index_selected
    chosen_index_selected = index


def RefreshChosenList(my_list):
    # print(my_list)
    index = 0
    listeChosenVideos.delete(0, END)
    for item in my_list:
        index += 1
        listeChosenVideos.insert(index, item)


def Call_for_SQL_Insertion():
    side = left_frame_value_side.get()
    color = left_frame_value_color.get()
    title = right_frame_value_title.get()

    if side != "" and color != "" and title != "":
        liste_dynamique_mod.TotalToSql(title, side, color)
        messagebox.showinfo("Info", "Sequence ajoutée")
        ref_sequence()
        mod_sequence.destroy()
    else:
        messagebox.showerror("Erreur de remplissage", "Remplissez bien tous les champs, dont le titre")


def Test_List_To_Video():
    list_videos_to_test = liste_dynamique_mod.return_list()
    tests_passed = True
    # here, write the tests and modify message box ... (to check ie that every color is the same ... )
    if messagebox.askokcancel("Rapport",
                              message="Sequence Valide (ou non pour l'instant). Voulez vous la jouer ? "):
        list_adresses = []
        for item in list_videos_to_test:
            list_adresses.append('/Videos/' + item[0][5])
        print(list_adresses)
        MovieManager.multiple_different_videos(list_adresses)


mod_sequence = Tk()
mod_sequence.title("Module de modification de séquences")
# window.geometry("1080x720")
mod_sequence.minsize(1080, 720)
mod_sequence.maxsize(1080, 720)
mod_sequence.iconbitmap("pictures/likeBlack.ico")
mod_sequence.config(background='#FFFFFF')

Titre_ajouter = Label(mod_sequence, text="Modification de la séquence", font=("Helvetica", 14), bg="white",
                      fg="black");
Titre_ajouter.pack()

items_frame = Frame(mod_sequence, bg="#FFFFFF", border=1)
items_frame.pack()

left_frame_t = Frame(items_frame, border=1)

left_frame_text_side_grid = Frame(left_frame_t)
left_frame_text_side = Label(left_frame_text_side_grid, text="Côté (g ou d) :", font=("Helvetica", 14),
                             fg="black");
left_frame_text_side.pack()
left_frame_text_side_grid.grid(row=0, column=0)

left_frame_value_side_grid = Frame(left_frame_t)
left_frame_value_side = Entry(left_frame_value_side_grid, width=3)
left_frame_value_side.pack()
left_frame_value_side.bind('<FocusOut>', SideAndColorChoseEvent)
left_frame_value_side.bind('<Return>', SideAndColorChoseEvent)
left_frame_value_side_grid.grid(row=0, column=1)

left_frame_text_color_grid = Frame(left_frame_t)
left_frame_text_color = Label(left_frame_text_color_grid, text="Couleur (j,b,m ou n) :", font=("Helvetica", 14),
                              fg="black");
left_frame_text_color.pack()
left_frame_text_color_grid.grid(row=0, column=2)

left_frame_value_color_grid = Frame(left_frame_t)
left_frame_value_color = Entry(left_frame_value_color_grid, width=3)
left_frame_value_color.pack()
left_frame_value_color.bind('<FocusOut>', SideAndColorChoseEvent)
left_frame_value_color.bind('<Return>', SideAndColorChoseEvent)
left_frame_value_color_grid.grid(row=0, column=3)

list_of_vid_frame = Frame(left_frame_t, bg="#FFF0F0", border=2)

scrollbar = Scrollbar(list_of_vid_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listeVideos = Listbox(list_of_vid_frame)
listeVideos.configure(width=90, height=35)
listeVideos.bind('<<ListboxSelect>>', OnSelectList)

my_list = SQLManager.readAll()
print("Ma liste dans VM " + str(my_list))
for item in my_list:
    label_in_list = str(item[0]) + " : >" + item[1] + "< Coté : >" + item[2] + "< Couleur : >" + item[
        3] + "< Longueur : >" + str(item[4]) + "< Fichier : >" + item[5] + "< Date : >" + str(item[6])
    listeVideos.insert(item[0], label_in_list)

# attach listbox to scrollbar
listeVideos.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listeVideos.yview)
list_of_vid_frame.grid(row=1, column=0, columnspan=4)
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

right_frame_text_title_grid = Frame(right_frame_t)
right_frame_text_title = Label(right_frame_text_title_grid, text="Titre : ", font=("Helvetica", 14),
                               fg="black");
right_frame_text_title.pack()
right_frame_text_title_grid.grid(row=0, column=0)

right_frame_value_title_grid = Frame(right_frame_t)
right_frame_value_title = Entry(right_frame_value_title_grid, width=30)
right_frame_value_title.pack()
right_frame_value_title_grid.grid(row=0, column=1)

list_of_selected_vids_grid = Frame(right_frame_t)

list_of_chosen_vid_frame = Frame(list_of_selected_vids_grid, bg="#FFF0F0", border=2)

scrollbar_chosen_list = Scrollbar(list_of_chosen_vid_frame)
scrollbar_chosen_list.pack(side=RIGHT, fill=Y)

listeChosenVideos = Listbox(list_of_chosen_vid_frame)
listeChosenVideos.configure(width=60, height=35)
listeChosenVideos.bind('<<ListboxSelect>>', OnSelectChosenList)

my_list = [[1, "Vide"]]
for item in my_list:
    label_in_list = str(item[0]) + " : >" + item[1]
    listeChosenVideos.insert(item[0], label_in_list)

# attach listbox to scrollbar
listeChosenVideos.config(yscrollcommand=scrollbar_chosen_list.set)
scrollbar_chosen_list.config(command=listeChosenVideos.yview)
list_of_chosen_vid_frame.grid(row=1, column=0, columnspan=4)
listeChosenVideos.pack()

list_of_selected_vids_grid.grid(row=1, column=0, columnspan=2)

right_frame_t.grid(row=0, column=2)

spacer = Label(mod_sequence, text="", font=("Helvetica", 10), fg="black");
spacer.pack()

buttons_frame = Frame(mod_sequence, border=1)
button_val_t = Frame(buttons_frame, padx=20)
button_val = Button(button_val_t, text="Valider", command=Call_for_SQL_Insertion)
button_val.pack()
button_val_t.grid(row=0, column=0)

button_test_t = Frame(buttons_frame, padx=20)
button_test = Button(button_test_t, text="Test", command=Test_List_To_Video)
button_test.pack()
button_test_t.grid(row=0, column=1)

button_dismiss_t = Frame(buttons_frame, padx=20)
button_dismiss = Button(button_dismiss_t, text="Annuler", command=mod_sequence.destroy)
button_dismiss.pack()
button_dismiss_t.grid(row=0, column=2)

texte_duree = Label(buttons_frame, text="                  Durée = ", font=("Helvetica", 12), fg="black");
texte_duree.grid(row=0, column=3)

buttons_frame.pack()

feed_fields_from_db()  # call the corresponding function that will fullfill fields from SQLDataBase

mod_sequence.mainloop()
ref_sequence()