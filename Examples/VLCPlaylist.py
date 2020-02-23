import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

import vlc
import time
my_list = ['VID_20200216_165431.mp4','VID_20200216_165431.mp4']
instance = vlc.Instance()
player = instance.media_player_new()
player.set_fullscreen(True)
playing = set([1,2,3,4])
for i in my_list:
    player.set_mrl(i)
    player.play()
    play=True
    while play == True:
        time.sleep(0.01)
        play_state = player.get_state()
        if play_state in playing:
            continue
        else:
            play = False