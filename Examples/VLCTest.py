import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
from time import sleep

class Player():
    def __init__(self):
        self._instance = vlc.Instance(['--video-on-top'])
        self._player = self._instance.media_player_new()
        self._player.set_fullscreen(True)

    def play(self, path):
        media = self._instance.media_new(path)
        self._player.set_media(media)
        self._player.play()

    def stop(self):
        self._player.stop()

myPlayer=Player()
myPlayer.play("VID_20200216_165431.mp4")

sleep(2) # Or however long you expect it to take to open vlc
