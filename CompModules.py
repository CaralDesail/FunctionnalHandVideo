from tkinter import *
from tkinter import ttk

def about_window():
    window_Ab = Tk()

    window_Ab.title("A propos")
    # window.geometry("1080x720")
    window_Ab.minsize(600, 400)
    window_Ab.iconbitmap("pictures/likeBlack.ico")
    window_Ab.config(background='#FFFFFF')

    top_title = Label(window_Ab, text="Functionnal POV Therapy V0.35",font=("Helvetica", 14), bg="white", fg="black");
    top_title.pack()
    phrase_recap = Label(window_Ab, text="\n\nDispositif expérimental sur une idée originale de Clément Varnier \n et "
                                         "développée par l'équipe d'innovation du CH Tullins :  \n[liste avec rôles dans"
                                         " le projet] \n",
                             font=("Helvetica", 10), bg="white", fg="black");
    phrase_recap.pack()
    phrase_logo = Label(window_Ab, text="\n \n\nLogo du CH" ,
                             font=("Helvetica", 14), bg="white", fg="black");
    phrase_logo.pack()

    phrase_credits_images = Label(window_Ab, text="\n\n\nIcons made by Darius Dan : https://www.flaticon.com/authors/darius-dan" ,
                             font=("Helvetica", 10), bg="white", fg="black");
    phrase_credits_images.pack()

    window_Ab.mainloop()

