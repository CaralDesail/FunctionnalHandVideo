from tkinter import *


def clic_action():
    print("Ok cliqué interne")


# create fiirst window
window = Tk()

window.title("Functionnal Video Therapy")
# window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("pictures/CyberArm.ico")
window.config(background='white')

# different frames
top_frame = Frame(window, bg="white", bd=1, relief=SUNKEN)
first_frame = Frame(window, bg="white", bd=1, relief=SUNKEN)

# in top frame :
label_title = Label(top_frame, text="Functionnal Video Therapy", font=("Courrier", 20), bg='white', fg="black")
label_title.pack(side=TOP)

label_subtitle = Label(first_frame, text="Information", font=("Courrier", 15), bg='white', fg="black")
label_subtitle.pack(side=TOP)

# in first_frame:
yt_button = Button(first_frame, text="Selectionner côté", font=("Courrier", 15), bg='grey', fg="black",
                   command=clic_action)
yt_button.pack(pady=25, padx=25, fill=X)

# add topframe
top_frame.pack()
first_frame.pack(side=LEFT)

# shows it in main loop
window.mainloop()
