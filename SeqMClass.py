import SQLManager


class MySequence:
    """The class will define the sequence of videos to use as a playlist and will contain it's name, total length
    number of items, and the list of videos references"""

    def __init__(self):
        self.caracteristique = "liste"
        self.name="NoName"
        self.totallist=[]
        self.actionList=[]
        self.length=int(0)

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

    def generate_actionlist_from_list(self):
        self.actionList=[]
        for item in self.totallist:
            self.actionList.append(item[0][1])
        return (self.actionList)

    def calcul_total_len(self):
        self.length=0
        for item in self.totallist:
            self.length+=int(item[0][4])
        return (self.length)

    def TotalToSql(self, name, side, color):

        localactionList=self.generate_actionlist_from_list()

        print('le nom:',name,' le cote ', side, 'la couleur ' , color)
        print ('et la liste', localactionList)

        print('et la longueur est',self.length)
        SQLManager.ajout_dyn_sequence(name,color,side,str(self.length),localactionList)

