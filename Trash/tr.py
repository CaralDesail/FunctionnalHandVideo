list_of_chosen_vid_frame = Frame(left_frame_t, bg="#FFF0F0", border=2)

scrollbar_chosen_list = Scrollbar(list_of_chosen_vid_frame)
scrollbar_chosen_list.pack(side=RIGHT, fill=Y)

listeChosenVideos = Listbox(list_of_chosen_vid_frame)
listeChosenVideos.configure(width=90, height=35)
listeChosenVideos.bind('<<ListboxSelect>>', OnSelectList)

my_list=SQLManager.readAll()
print("Ma liste dans VM "+str(my_list))
for item in my_list:
    label_in_list=str(item[0])+" : >"+item[1]+"< Coté : >"+item[2]+"< Couleur : >"+item[3]+"< Longueur : >"+str(item[4])+"< Fichier : >"+item[5]+"< Date : >"+str(item[6])
    listeChosenVideos.insert(item[0], label_in_list)

# attach listbox to scrollbar
listeChosenVideos.config(yscrollcommand=scrollbar_chosen_list.set)
scrollbar_chosen_list.config(command=listeChosenVideos.yview)
list_of_chosen_vid_frame.grid(row=1, column=0, columnspan=4)
listeChosenVideos.pack()