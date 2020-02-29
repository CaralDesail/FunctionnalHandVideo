"""
 * Functionnal Video Therapy
 * Version - 0.3
 * All right reserved
 *
 * Copyright (c) 2019 Alain Carrot for the coding part,
 * Tullins's innovation team for the concept.
 */
"""

from tkinter import *
from tkinter import ttk
import SQLManager
import os
import MovieManager
import subprocess
import CompModules

handSideClic = "0"
colorChoosen = "0"
list_indiv_combobox = ["Selectionnez une action", "Pen", "Spoon", "Cut", "Piano"]
LeftSelectedAction = ""
#

def video_management_opening():  # in menu
    print("Ouverture du gestionnaire de videos")
    subprocess.call("python VideoManagement.py")
     # call other windows that contain video manager

def repertoire_videos():  # in menu
    print("ouverture du repertoire des videos")
    path = "Videos"
    path = os.path.realpath(path)
    os.startfile(path)

def sequences_management_opening(): #in menu, will call Sequences Management
    print("Ouverture du gestionnaire de séquences")
    subprocess.call("python SequencesManagement.py")

def about_call(): #call a function in CompModules that will show a window with Credits
    CompModules.about_window()

# about side choosen : the clic will call clic_main gauche or droite that will call Side Hand Clic Action, that will finaly call ChoseIntegrator
def clic_main_gauche():
    Side_Hand_Clic_Action("gauche")


def clic_main_droite():
    Side_Hand_Clic_Action("droite")


def Side_Hand_Clic_Action(cote_Clic):
    global handSideClic
    if cote_Clic == "droite":  # if boolean right hand Clic then :

        handSideClic = "d"
        Left_Hand_button.config(image=picture_left_hand_i)
        Right_Hand_button.config(image=picture_right_hand_a)

    else:
        handSideClic = "g"
        Left_Hand_button.config(image=picture_left_hand_a)
        Right_Hand_button.config(image=picture_right_hand_i)
    Chose_Integrator()


def clic_yellow():
    global colorChoosen
    colorChoosen = "j"
    Color_Yellow_button.config(image=picture_Color_Yellow_a)
    Color_White_button.config(image=picture_Color_White_i)
    Color_Marron_button.config(image=picture_Color_Marron_i)
    Color_Black_button.config(image=picture_Color_Black_i)
    Chose_Integrator()


def clic_white():
    global colorChoosen
    colorChoosen = "b"
    Color_Yellow_button.config(image=picture_Color_Yellow_i)
    Color_White_button.config(image=picture_Color_White_a)
    Color_Marron_button.config(image=picture_Color_Marron_i)
    Color_Black_button.config(image=picture_Color_Black_i)
    Chose_Integrator()


def clic_marron():
    global colorChoosen
    colorChoosen = "m"
    Color_Yellow_button.config(image=picture_Color_Yellow_i)
    Color_White_button.config(image=picture_Color_White_i)
    Color_Marron_button.config(image=picture_Color_Marron_a)
    Color_Black_button.config(image=picture_Color_Black_i)
    Chose_Integrator()


def clic_black():
    global colorChoosen
    colorChoosen = "n"
    Color_Yellow_button.config(image=picture_Color_Yellow_i)
    Color_White_button.config(image=picture_Color_White_i)
    Color_Marron_button.config(image=picture_Color_Marron_i)
    Color_Black_button.config(image=picture_Color_Black_a)
    Chose_Integrator()


def Chose_Integrator():  # will use the side and the color to manage the Combobox content
    print("main ", handSideClic, " ", colorChoosen)
    selectedList = SQLManager.tri_and_title(handSideClic, colorChoosen)  # select solo items with good color and side
    print("liste totale : ", selectedList)  # and print this list
    # if (handSideClic!="0" and colorChoosen !="0"):
    #    print(selectedList[0][1])
    list_for_solo_combobox = []
    for i in selectedList:  # create a new list for combobox
        list_for_solo_combobox.append(i[1]) #i[1] is the Title of action
    left_frame_combobox.configure(values=list_for_solo_combobox)

    list_for_sequence_combobox=SQLManager.sort_sequences_by_color_side_to_names(colorChoosen,handSideClic)
    right_frame_combobox.configure(values=list_for_sequence_combobox)

def All_Choosen_So_URL_Video():  # will return the corresponding Path to video
    listOfItemSelected = SQLManager.retrive_video_path(LeftSelectedAction, handSideClic, colorChoosen)
    pathSelected=listOfItemSelected[0][5]
    return pathSelected


def left_combo_action(event):  # function called when left combobox changes
    global LeftSelectedAction
    LeftSelectedAction = left_frame_combobox.get()
    print(LeftSelectedAction)


def ValidateLeftFrame():  # function called when Button in left frame is clicked
    print(All_Choosen_So_URL_Video())
    VideoURL=All_Choosen_So_URL_Video()
    MovieManager.video_launch(VideoURL) #if vlc is not available, you can use MovieManager.video_launch(VideoURL) with moviepy



def right_combo_action(event):
    global RightSelectedAction
    RightSelectedAction = right_frame_combobox.get()
    Sequence_Chosen = SQLManager.retrive_sequence(RightSelectedAction, handSideClic, colorChoosen)  # retrive spec of chosen seq
    sec_to_min=Sequence_Chosen[0][4]/60 #convert to min
    duration = "Durée : "+str(sec_to_min)+" min" #convert in a string
    scheme=Sequence_Chosen[0][5] #will retrive the scheme / An other function to factorise the sheme would be interesting to develop
#insert here the changes in text fields.
    right_frame_text_length.configure(text=duration) #write duration in text field
    right_frame_text_scheme.configure(text=scheme) #write schema in text field

    print(RightSelectedAction)


def ValidateRightFrame():  # function called when Button in right frame is clicked
    #print("Right FrameVal")
    Sequence_Chosen=SQLManager.retrive_sequence(RightSelectedAction,handSideClic,colorChoosen) #item select
    #print("La séquence choisie :", Sequence_Chosen)
    list_of_actions_to_play=SQLManager.sequence_to_list(Sequence_Chosen) #then retrive list of names
    list_of_filepath = SQLManager.find_by_id_to_filename_list(list_of_actions_to_play, handSideClic, colorChoosen) #retrive the filename lsit
    #print("La liste des adresses : ",list_of_filepath)
    MovieManager.multiple_different_videos(list_of_filepath)


### UI with Tkinter
###################


# create first window
window = Tk()

window.title("Functionnal Therapy POV")
# window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("pictures/likeBlack.ico")
window.config(background='#FFFFFF')

# frame du titre
title_frame = Frame(window)
titlebar = PhotoImage(file=r"pictures/UI/gif/Barre_Titre.gif")
widthI = 1080
heightI = 100  # 58 is the fitting size
canvas = Canvas(title_frame, width=widthI, height=heightI, bg="#FFFFFF", bd=0, highlightthickness=0)
canvas.create_image(widthI / 2, 40, image=titlebar)
canvas.grid(row=0, column=0)

# frame du choix de main
top_frame = Frame(window)
# a l'interieur, les deux grids pour les deux boutons
right_frame_h = Frame(top_frame, bg="#FFFFFF", pady=20)
right_frame_h.grid(row=0, column=1)
picture_right_hand_i = PhotoImage(file=r"pictures/UI/gif/UI_MD_i.gif")  # picture charged when button is not clicked
picture_right_hand_a = PhotoImage(file=r"pictures/UI/gif/UI_MD_a.gif")  # picture charged when button is  clicked
Right_Hand_button = Button(right_frame_h, bg="white", image=picture_right_hand_i, border=0,
                           command=clic_main_droite);
Right_Hand_button.pack()
left_frame_h = Frame(top_frame, bg="#FFFFFF", pady=20)
left_frame_h.grid(row=0, column=0)
picture_left_hand_i = PhotoImage(file=r"pictures/UI/gif/UI_MG_i.gif")  # picture charged when button is not clicked
picture_left_hand_a = PhotoImage(file=r"pictures/UI/gif/UI_MG_a.gif")  # picture charged when button is clicked
Left_Hand_button = Button(left_frame_h, bg="white", image=picture_left_hand_i, border=0,
                          command=clic_main_gauche);
Left_Hand_button.pack()

###
# frame au dessous, de la couleur
###
color_frame = Frame(window)
# boutons en question
Color_Yellow_frame = Frame(color_frame, padx=10, bg="white")
Color_Yellow_frame.grid(row=0, column=0)
picture_Color_Yellow_i = PhotoImage(file=r"pictures/UI/gif/UI_J_i.gif")  # picture charged when button is not clicked
picture_Color_Yellow_a = PhotoImage(file=r"pictures/UI/gif/UI_J_a.gif")
Color_Yellow_button = Button(Color_Yellow_frame, text="-", image=picture_Color_Yellow_i, fg="black", border=0,
                             bg="white",
                             command=clic_yellow);
Color_Yellow_button.pack(fill=X)

Color_White_frame = Frame(color_frame, padx=10, bg="white")
Color_White_frame.grid(row=0, column=1)
picture_Color_White_i = PhotoImage(file=r"pictures/UI/gif/UI_R_i.gif")  # picture charged when button is not clicked
picture_Color_White_a = PhotoImage(file=r"pictures/UI/gif/UI_R_a.gif")
Color_White_button = Button(Color_White_frame, text="-", image=picture_Color_White_i, fg="black", border=0, bg="white",
                            command=clic_white);
Color_White_button.pack(fill=X)

Color_Marron_frame = Frame(color_frame, padx=10, bg="white")
Color_Marron_frame.grid(row=0, column=2)
picture_Color_Marron_i = PhotoImage(file=r"pictures/UI/gif/UI_M_i.gif")  # picture charged when button is not clicked
picture_Color_Marron_a = PhotoImage(file=r"pictures/UI/gif/UI_M_a.gif")
Color_Marron_button = Button(Color_Marron_frame, text="-", image=picture_Color_Marron_i, fg="black", border=0,
                             bg="white",
                             command=clic_marron);
Color_Marron_button.pack(fill=X)

Color_Black_frame = Frame(color_frame, padx=10, bg="white")
Color_Black_frame.grid(row=0, column=3)
picture_Color_Black_i = PhotoImage(file=r"pictures/UI/gif/UI_B_i.gif")  # picture charged when button is not clicked
picture_Color_Black_a = PhotoImage(file=r"pictures/UI/gif/UI_B_a.gif")
Color_Black_button = Button(Color_Black_frame, text="-", image=picture_Color_Black_i, fg="black", border=0, bg="white",
                            command=clic_black);
Color_Black_button.pack(fill=X)

###
# frame englobant les deux cadres de selection des actions
###
main_action_frame = Frame(window)
validate_pic = PhotoImage(file=r"pictures/UI/gif/UI_Lancer.gif")  # the picture for validate button in both cases

# frame de gauche
left_frame = Frame(main_action_frame, bg="#FFFFFF", border=1)

left_frame.grid(row=0, column=0)

left_frame_title = Label(left_frame, text="         Action individuelle :                             ",
                         font=("Helvetica", 20), bg="white", fg="black");
left_frame_title.pack()

left_frame_spacer1 = Label(left_frame, text="", font=("Helvetica", 20), bg="white", fg="black");
left_frame_spacer1.pack()

left_frame_combobox = ttk.Combobox(left_frame, values=list_indiv_combobox, font=("Helvetica", 14), state="readonly",
                                   height=7)
left_frame_combobox.current(0)
left_frame_combobox.bind("<<ComboboxSelected>>", left_combo_action)
left_frame_combobox.pack()
left_frame_spacer2 = Label(left_frame, text="", font=("Helvetica", 63), bg="white", fg="black");
left_frame_spacer2.pack()

Left_Frame_button = Button(left_frame, text="Valider", image=validate_pic, border=0,
                           command=ValidateLeftFrame);
Left_Frame_button.pack()

# frame de droite
right_frame = Frame(main_action_frame, bg="#FFFFFF", border=1)
right_frame.grid(row=0, column=1)
right_frame_title = Label(right_frame, text="           Séquence :                                      ",
                          font=("Helvetica", 20), bg="white", fg="black");
right_frame_title.pack()
right_frame_spacer1 = Label(right_frame, text="", font=("Helvetica", 20), bg="white", fg="black");
right_frame_spacer1.pack()
list_sequence_combobox = ["Selectionnez la séquence", "Liste Perso 1", "Liste Longue Perso", "Liste Courte Perso",
                          "Ecriture intensive"]
right_frame_combobox = ttk.Combobox(right_frame, values=list_sequence_combobox, font=("Helvetica", 14),
                                    state="readonly", height=7)
right_frame_combobox.current(0)
right_frame_combobox.bind("<<ComboboxSelected>>", right_combo_action)
right_frame_combobox.pack()
right_frame_spacer1b = Label(right_frame, text="", font=("Helvetica", 15), bg="white", fg="black");
right_frame_spacer1b.pack()
right_frame_text_length = Label(right_frame, text="Durée : ", font=("Helvetica", 14), bg="white", fg="black");
right_frame_text_length.pack()
right_frame_text_scheme = Label(right_frame, text="Schema : ", font=("Helvetica", 8), bg="white", fg="black");
right_frame_text_scheme.pack()
right_frame_spacer2 = Label(right_frame, text="", font=("Helvetica", 10), bg="white", fg="black");
right_frame_spacer2.pack()
Right_Frame_button = Button(right_frame, text="Valider", image=validate_pic, border=0,
                            command=ValidateRightFrame);
Right_Frame_button.pack()

# creation barre de menus
menu_bar = Menu(window)
# creer premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Gestion des videos", command=video_management_opening)
file_menu.add_command(label="Répertoire des vidéos", command=repertoire_videos)
file_menu.add_command(label="Gestion des Séquences", command=sequences_management_opening)

aide_menu = Menu(menu_bar, tearoff=0)
aide_menu.add_command(label="Manuel d'utilisateur")
aide_menu.add_command(label="Manuel d'administrateur")
aide_menu.add_command(label="Crédits", command=about_call)

menu_bar.add_cascade(label="Outils", menu=file_menu)
menu_bar.add_cascade(label="Aide", menu=aide_menu)
menu_bar.add_command(label="Quitter", command=window.quit)

title_frame.pack(expand=NO, fill=BOTH)
top_frame.pack(expand=NO)
color_frame.pack(expand=NO)
main_action_frame.pack(expand=YES, fill=X)
# configurer la fenetre pour ajouter la menu bar
window.config(menu=menu_bar)

# shows it in main loop
window.mainloop()
