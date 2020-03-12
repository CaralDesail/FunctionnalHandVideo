import sqlite3


def listToString(s):
    # initialize an empty string
    str1 = ";"

    # return string
    return (str1.join(s))


#################################
##On table list_of_videos
#################################


def readAll():  # a way to print database
    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM list_of_videos")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r)
    """cursor.execute("SELECT * FROM list_of_videos")
    print("\nfetch one:")
    res = cursor.fetchone()
    print(res)"""
    connection.close()
    return result

def create_db():  # if database lost
    connection = sqlite3.connect("video_db.db")

    cursor = connection.cursor()

    # delete
    # cursor.execute("""DROP TABLE employee;""")

    sql_command = """
    CREATE TABLE list_of_videos ( 
    id_video INTEGER PRIMARY KEY, 
    action_name VARCHAR(30), 
    hand CHAR(1),
    color CHAR(1), 
    length INTEGER,
    filename CHAR(30),
    date DATE);"""
    cursor.execute(sql_command)

    # never forget this, if you want the changes to be saved:
    connection.commit()

    connection.close()


def ajout_dyn(action_name, hand, color, length, filename):  # will add new entry in database
    action_name = action_name
    hand = hand
    color = color
    length = length
    filename = filename
    date = "2020-02-15"

    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()

    format_str = """INSERT INTO list_of_videos ( action_name, hand, color, length,filename, date)
        VALUES (?, ?, ?, ?,?,?);"""

    cursor.execute(format_str, (action_name, hand, color, length, filename, date))
    connection.commit()
    connection.close()


#ajout_dyn("test2","g","b","8000","VID_20200216_165505.mp4")

def delete_vid(id_of_object):  # will add new entry in database

    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()

    format_str = """DELETE FROM list_of_videos WHERE id_video=?"""

    cursor.execute(format_str, (id_of_object,))
    print("Suppression de l'item n°",id_of_object)
    connection.commit()
    connection.close()

def find_vid_by_id(id_of_object):  # will find video through id

    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()

    format_str = """SELECT * FROM list_of_videos WHERE id_video=?"""

    cursor.execute(format_str, (id_of_object,))
    print("Recupération de l'item n°",id_of_object)
    result = cursor.fetchall()
    connection.close()
    return result

def tri_and_title(side, color):
    HandSide = side
    HandColor = color

    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()
    cursor.execute(("SELECT * FROM list_of_videos WHERE hand ==? AND color==?"), (HandSide, HandColor))
    result = cursor.fetchall()
    # for r in result:
    #   print(r)
    return result

    connection.close()


# tri_and_title("l","w")

def retrive_video_path(action, side, color): #find the  video (and path) according to actionname, side and color
    ActionChosen = action
    HandSide = side
    HandColor = color

    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()
    cursor.execute(("SELECT * FROM list_of_videos WHERE hand ==? AND color==? AND action_name==?"),
                   (HandSide, HandColor, ActionChosen))
    result = cursor.fetchall()
    # for r in result:
    #   print(r)
    return result

    connection.close()

def find_by_id_to_filename_list(list_of_actions,side, color): #takes the list of id(2,4,3,2) and create a new list with path of videos
    HandSide = side
    HandColor = color

    list_to_return=[] #the name of the list with filename
    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()

    for ActionChosen in list_of_actions:
        cursor.execute(("SELECT * FROM list_of_videos WHERE hand ==? AND color==? AND action_name==?"),
                       (HandSide, HandColor, ActionChosen))
        result = cursor.fetchone()

        if result == None: #if one action is missing ...
            print("Erreur : ",ActionChosen," n'existe pas, au moins dans cette configuration latéralité/couleur")
        else: #if action is found, then append the list to return with the filename
            result_filename="Videos/"+result[5] # takes only the filename in the entire spec of selected line
            list_to_return.append(result_filename)

    return list_to_return

    connection.close()



#################################
#################################
#################################

##On table list_of_sequences

#################################
#################################
#################################

def spec_from_id(id):
    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()
    cursor.execute(("SELECT * FROM list_of_sequences WHERE id_sequence ==%s ")%
                   (id))

    result = cursor.fetchall()
    for r in result:
       print("Depuis module SQLMan: ",r)
    return result
    connection.close()

def retrive_sequence(sequence_name, side, color): #find the pâth of a video according to actionname, side and color
    HandSide = side
    HandColor = color

    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()
    cursor.execute(("SELECT * FROM list_of_sequences WHERE hand ==? AND color==? AND sequence_name==?"),
                   (HandSide, HandColor, sequence_name))
    result = cursor.fetchall()
    for r in result:
       print(r)
    return result
    connection.close()

#retrive_sequence("2Styl","r","w")

def list_of_sequence():  # find all sequences

    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()
    cursor.execute(("SELECT * FROM list_of_sequences "),
                   ())
    result = cursor.fetchall()
    for r in result:
        print(r)
    return result
    connection.close()


def sequence_to_list(sequence): #will give a list of videos from selected sequence
    print("entree en moulinette:",sequence[0][5])
    string_to_convert=sequence[0][5]
    list_to_return=string_to_convert.split(";")
    print("apres la moul, la liste : ", list_to_return)
    return list_to_return

def ajout_dyn_sequence(sequence_name,color, hand, duration, schema):  # will add new entry in database
    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()

    format_str = """INSERT INTO list_of_sequences (sequence_name,color, hand, duration, schema)
        VALUES (?, ?, ?, ? ,?);"""

    cursor.execute(format_str, (sequence_name,color, hand, duration, listToString(schema)))
    connection.commit()
    connection.close()

#list_to_test=["Stylo","Stylo"]
#ajout_dyn_sequence("2Styl","w","l","600",list_to_test)

def sort_sequences_by_color_side_to_names(color,hand): #will return a lost of names of found sequences that fit

    list_of_names=[]
    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()
    cursor.execute(("SELECT * FROM list_of_sequences WHERE hand ==? AND color==?"),
                   (hand, color))
    result = cursor.fetchall()

    for r in result:
        list_of_names.append(r[1])
    print("liste des noms des séquences sélectionnées : ",list_of_names)
    return list_of_names

    connection.close()

#sort_sequences_by_color_side_to_names("w","r")

def delete_seq(id_of_object):  # will add new entry in database

    connection = sqlite3.connect("video_db.db")
    cursor = connection.cursor()

    format_str = """DELETE FROM list_of_sequences WHERE id_sequence=%s"""


    cursor.execute(format_str%(id_of_object,))
    print("Suppression de l'item n°",id_of_object)
    connection.commit()
    connection.close()


