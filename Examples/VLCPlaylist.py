import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc


Instance = vlc.Instance('--fullscreen')
player = Instance.media_player_new()
Media = Instance.media_new('VID_20200216_165431.mp4')
Media.get_mrl()
player.set_media(Media)
player.set_fullscreen(True)
player.play()
from time import sleep

sleep(2) # Or however long you expect it to take to open vlc
while player.is_playing():
     sleep(0.001)