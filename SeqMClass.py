import SQLManager

class MySequence:
    """The class will define the sequence of videos to use as a playlist and will contain it's name, total length
    number of items, and the list of videos references"""
    nombre_objets=0
    def __init__(self):
        MySequence.nombre_objets += 1

        if MySequence.nombre_objets >=2:
            print("attention, destruction objets")


my_sequence1=MySequence()
my_sequence2=MySequence()