
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
from time import sleep

#will select if you want to use MoviePyLib of VLC Lib
MoviePyUse=False
if MoviePyUse: # we use moviepy
    import pygame
    from moviepy.editor import *
else : #we use vlc
    import vlc




def video_launch(file): # version of mediaplayer through vlc
    print (file)

    if MoviePyUse:
        stringFile = "Videos/" + file
        clip = VideoFileClip(stringFile)
        clip.preview(fullscreen=True)
        pygame.quit()

    else:

        Instance = vlc.Instance()
        player = Instance.media_player_new()
        stringFile = "Videos/" + file
        Media = Instance.media_new(stringFile)
        Media.get_mrl()
        print("la valeur du get :",Media.get_mrl())

        player.set_media(Media)
        player.set_fullscreen(True)
        player.play() # launch player and file
        sleep(2)
        print(player.get_length())
        if player.get_length()<=0:
            print("Fichier non trouvé ou défaillant")
        while player.is_playing(): #wait until file's end
                sleep(0.2)
        player.stop()

#video_launch("VID_20200216_165449.mp4")


def multiple_different_videos(listOfFiles):  # plays a list in order (automatic playlist)
    if MoviePyUse:
        for i in listOfFiles:
            clip = VideoFileClip(i)
            clip.preview()
        pygame.quit

    else: #we use vlc
        my_list = listOfFiles
        instance = vlc.Instance()
        player = instance.media_player_new()
        player.set_fullscreen(True)
        playing = set([1, 2, 3, 4])
        for i in range(len(my_list)):
            player.set_mrl(my_list[i])
            player.play()
            play = True
            while play == True:
                sleep(0.001)
                # print("longueur du clip : ",player.get_length()," numéro du clip : ", i)
                play_state = player.get_state()
                if play_state in playing:
                    if ((i + 1) == len(my_list)):  # if it's the last clip of the list
                        sleep(1)  # wait the last video to be initialised
                        print("dernier clip, processus de fin initialisé")
                        sleep((player.get_length() / 1000) - 1)  # wait the last clip to be played
                        print("fin du dernier clip")
                        player.stop()  # kills player
                        play = False  # and stop while loop
                    continue
                else:
                    play = False

"""
    old code to show range of files:
    for index in range(len(listOfFiles)):
        print(index," et le nom : ",listOfFiles[index])
        clip=VideoFileClip(listOfFiles[index])
        clip.preview()
"""

# multiple_different_videos(["Videos/VID_20200216_165449.mp4","Videos/VID_20200216_165431.mp4"])
