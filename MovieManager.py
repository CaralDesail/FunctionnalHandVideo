from moviepy.editor import *
import pygame
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
from time import sleep

def video_launch(file): #version of mediaplayer through moviepy
    stringFile = "Videos/" + file
    clip = VideoFileClip(stringFile)
    clip.preview(fullscreen=True)
    pygame.quit()


# video_launch("VID_20200216_165449.mp4")

def video_launch_vlc(file): # version of mediaplayer through vlc
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    stringFile = "Videos/" + file
    Media = Instance.media_new(stringFile)
    Media.get_mrl()

    player.set_media(Media)
    player.set_fullscreen(True)
    player.play() # launch player and file
    sleep(2)
    print(player.get_length())
    while player.is_playing(): #wait until file's end
            sleep(0.2)
    player.stop()

#video_launch_vlc("VID_20200216_165449.mp4")

def multiple_same_video(file, iterations):  # plays same file in loop (not very usefull if you use other multiple selection players
    stringFile = "Videos/" + file
    clip = VideoFileClip(stringFile)
    while iterations != 0:
        iterations -= 1
        print(iterations)
        clip.preview(fullscreen=True)
    pygame.quit()


# multiple_same_video("VID_20200216_165449.mp4",2)


def multiple_different_videos_old(listOfFiles):  # plays a list in order (manual feeding)

    stringFile1 = listOfFiles[0]
    stringFile2 = listOfFiles[1]
    clip1 = VideoFileClip(stringFile1)
    clip2 = VideoFileClip(stringFile2)
    clip2.preview()
    clip1.preview()
    clip2.preview()
    clip1.preview()
    pygame.quit()


def multiple_different_videos(listOfFiles):  # plays a list in order (automatic playlist)

    for i in listOfFiles:
        clip = VideoFileClip(i)
        clip.preview()
    pygame.quit


"""
    old code to show range of files:
    for index in range(len(listOfFiles)):
        print(index," et le nom : ",listOfFiles[index])
        clip=VideoFileClip(listOfFiles[index])
        clip.preview()
"""

# multiple_different_videos(["Videos/VID_20200216_165449.mp4","Videos/VID_20200216_165431.mp4"])
