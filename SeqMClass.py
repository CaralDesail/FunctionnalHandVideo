import SQLManager


class MySequence:
    """The class will define the sequence of videos to use as a playlist and will contain it's name, total length
    number of items, and the list of videos references"""

    def __init__(self):
        self.caracteristique = "liste"
        self.name="NoName"
        self.totallist=[]

    def new_name(self,nname): #function what will change the name of current list
        self.name=nname

    def addToList(self,item):
        self.totallist.append(item)
        self.show_list()

    def deleteFromList(self,id_of_item):
        self.totallist.pop(id_of_item)

    def up(self,id_to_up):
        previous_id=id_to_up-1
        self.totallist[previous_id], self.totallist[id_to_up]=self.totallist[id_to_up], self.totallist[previous_id]

    def down(self,id_to_dw):
        following_id=id_to_dw+1
        self.totallist[following_id], self.totallist[id_to_dw]=self.totallist[id_to_dw], self.totallist[following_id]

    def show_list(self):
        print(self.totallist)

    def return_list(self):
        return(self.totallist)

mysequence=MySequence()
print(mysequence.name)
mysequence.new_name("Ma séquence")
print(mysequence.name)
print(mysequence.totallist)
mysequence.addToList([1,1,2])
mysequence.addToList([2,2,3])
mysequence.addToList([5,5,7])
print(mysequence.totallist)
mysequence.up(1)
print(mysequence.totallist)
mysequence.up(2)
print(mysequence.totallist)
print("puis down")
mysequence.down(0)
print(mysequence.totallist)
mysequence.down(1)
print(mysequence.totallist)
