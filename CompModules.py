# coding: utf-8

from tkinter import *
from tkinter import ttk
import os
import SQLManager

def about_window():
    window_Ab = Tk()

    window_Ab.title("A propos")
    # window.geometry("1080x720")
    window_Ab.minsize(600, 400)
    window_Ab.maxsize(600, 400)
    window_Ab.iconbitmap("pictures/likeBlack.ico")
    window_Ab.config(background='#FFFFFF')

    top_title = Label(window_Ab, text="Functionnal POV Therapy V0.6",font=("Helvetica", 14), bg="white", fg="black");
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

def DBTest_Window():


    def test_videos_links():

        list_of_errors_in_videofiles=[]
        all_test_passed=True
        list_of_files_in_directory=os.listdir('Videos/')
        print(list_of_files_in_directory)
        list_of_video_entry_to_check=SQLManager.readAll()

        for entry in list_of_video_entry_to_check:
            if entry[5] in list_of_files_in_directory:
                video_found_in_directory=True
            else:
                video_found_in_directory=False
                messageErrorLog="Video [",entry[5],"] correspondant à l'item n°",entry," non trouvée dans le répertoire."
                print(messageErrorLog)
                list_of_errors_in_videofiles.append(messageErrorLog)
                all_test_passed=False


            print(video_found_in_directory)



        if all_test_passed==False:
            video_link_text.config(text="Fichiers video défaillants, voir le fichier ErrorLogs",foreground ="#FF0000" )
        else:
            video_link_text.config(text="Fichiers video OK")


        return list_of_errors_in_videofiles

    def test_sequences_coherence():

        list_of_errors_in_seq_coherence = []
        all_test_passed = True
        list_of_seq_entry_to_check = SQLManager.list_of_sequence()

        for entry in list_of_seq_entry_to_check:

            list_of_actions=entry[5].split(";")
            for action in list_of_actions:
                videoFound=SQLManager.retrive_video_path(action=action,side=entry[3],color=entry[2])
                print(videoFound)

                if videoFound==[]:
                    messageErrorLog="Sequence : ",entry," incomplète : Vidéo correspondant à l'action [",action,"] introuvable."
                    list_of_errors_in_seq_coherence.append(messageErrorLog)
                    all_test_passed = False
                    print(messageErrorLog)
            """
            if 1==True:
                all_test_passed = True
            else:
                messageErrorLog = "Video [", entry[
                    5], "] correspondant à l'item n°", entry, " non trouvée dans le répertoire."
                print(messageErrorLog)
                list_of_errors_in_seq_coherence.append(messageErrorLog)
                all_test_passed = False
            """

        if all_test_passed == False:
            seq_coherence_text.config(text="Sequences incohérentes, voir le fichier ErrorLogs", foreground="#FF0000")
        else:
            seq_coherence_text.config(text="Séquences OK")

        return list_of_errors_in_seq_coherence


    def WriteInErrorLog(ErrorVideofiles,ErrorSequenceCoherence):
        f = open("ErrorLog.txt", "w")
        ErrorVideofilesInString="\n".join(str(i) for i in ErrorVideofiles)
        if ErrorVideofilesInString=="":
            ErrorVideofilesInString="Tous les fichiers correspondants aux vidéos de la base de donnée ont été trouvés.\n"

        ErrorSequenceCoherenceInString="\n".join(str(i) for i in ErrorSequenceCoherence)
        if ErrorSequenceCoherenceInString=="":
            ErrorSequenceCoherenceInString="Toutes les vidéos appelées par les différentes séquences sont présentes dans la DB."

        total_string=ErrorVideofilesInString+"\n"+ErrorSequenceCoherenceInString

        f.write(total_string)

        f.close()

    Test_Window = Tk()

    Test_Window.title("Outil de test")
    # window.geometry("1080x720")
    Test_Window.minsize(600, 400)
    Test_Window.maxsize(600, 400)
    Test_Window.iconbitmap("pictures/likeBlack.ico")
    Test_Window.config(background='#FFFFFF')

    top_title = Label(Test_Window, text="Vérification de cohérence et d'intégrité de la base", font=("Helvetica", 14), bg="white", fg="black");
    top_title.pack()

    spacer = Label(Test_Window, text="\n \n\n" ,
                             font=("Helvetica", 14), bg="white", fg="black");
    spacer.pack()

    video_link_text = Label(Test_Window, text="Liens vidéo : " ,
                             font=("Helvetica", 10), bg="white", fg="black");
    video_link_text.pack()

    seq_coherence_text = Label(Test_Window, text="Analyse séquences : " ,
                             font=("Helvetica", 10), bg="white", fg="black");
    seq_coherence_text.pack()

    ErrorVideofiles=test_videos_links() # First tests, return a list of errors. Void if no error;
    ErrorSequenceCoherence=test_sequences_coherence() # will check if all videos corresponding to actions are present in DB

    WriteInErrorLog(ErrorVideofiles,ErrorSequenceCoherence)

    Test_Window.mainloop()

if __name__ == '__main__': # will call following function if the window is called directly (and not from soft main screen)
    DBTest_Window()
