Test_Window = Tk()

Test_Window.title("A propos")
# window.geometry("1080x720")
Test_Window.minsize(600, 400)
Test_Window.maxsize(600, 400)
Test_Window.iconbitmap("pictures/likeBlack.ico")
Test_Window.config(background='#FFFFFF')

top_title = Label(Test_Window, text="Functionnal POV Therapy V0.6", font=("Helvetica", 14), bg="white", fg="black");
top_title.pack()
phrase_recap = Label(Test_Window, text="\n\nDispositif expérimental sur une idée originale de Clément Varnier \n et "
                                     "développée par l'équipe d'innovation du CH Tullins :  \n[liste avec rôles dans"
                                     " le projet] \n",
                     font=("Helvetica", 10), bg="white", fg="black");
phrase_recap.pack()
phrase_logo = Label(Test_Window, text="\n \n\nLogo du CH",
                    font=("Helvetica", 14), bg="white", fg="black");
phrase_logo.pack()

phrase_credits_images = Label(Test_Window,
                              text="\n\n\nIcons made by Darius Dan : https://www.flaticon.com/authors/darius-dan",
                              font=("Helvetica", 10), bg="white", fg="black");
phrase_credits_images.pack()

Test_Window.mainloop()