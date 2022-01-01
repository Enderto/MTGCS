#library
import json,os
from tkinter import *
from pathlib import Path
from PIL import Image, ImageTk

#All the def

#search if the file existe or not
def fileok(path):
    files = Path(path)
    if files.is_file():
        return True
    else:
        return False

def nbc(n):
    for i in range(j["data"]["baseSetSize"]):
        if (j["data"]["cards"][i]["number"]==n):
            return i

#cut the description of the file to fit in the windows
def re(a):
    tmp = len(a)
    stmp = a.split() #"cut" the description
    if (tmp >5):
        for i in range(5,len(stmp),5):
            stmp.insert(i,"\n")#add a \n each 5 words
        fs = ' '.join(stmp)#join all again in one str
    else:
        fs = a
    return fs

#The searh of all the information
def card(a,b):

    x = open("json/"+a+".json","r")
    global j
    j = json.load(x)

    out=""
    types = j["data"]["cards"][b]["types"][0]

    out = out + "Name :\n"
    out = out + j["data"]["cards"][b]["name"]
    if (types!="Creature"):
        print("This a creature, there should be some code here later ^^")
    else:
        out = out+"\n------------------------------\nMana cost :\n"+j["data"]["cards"][b]["manaCost"]+"\n"

    out = out + "------------------------------\n"
    out = out + "Type :\n" + j["data"]["cards"][b]["originalType"]+"\n------------------------------\nSet code:\n"+j["data"]["cards"][b]["setCode"]+"\n"
    out = out + "------------------------------\n"
    out = out + "Description :\n" + re(j["data"]["cards"][b]["originalText"])+"\n"
    if (types=="Creature"):
        out = out + "------------------------------\nPower: \n"+j["data"]["cards"][b]["power"]+" / "+j["data"]["cards"][b]["toughness"]+"\n------------------------------\n"
    elif (types=="Planeswalker"):
        out = out + "-----------------------"+j["data"]["cards"][b]["loyalty"]+"-\n"
    out = out + "artist :\n" + j["data"]["cards"][b]["artist"]+"\n------------------------------\nnb from the set :\n"+str(j["data"]["cards"][b]["number"])+"/"+str(j["data"]["baseSetSize"])+"\n"
    #fin
    return out

#When the button is clicked
def ButtonClick():
    choice=""
    for i in Lb1.curselection():
        choice=Lb1.get(i)
    if fileok("json/"+choice+".json")==True:
        text['text']=card(choice,nbc(E1.get()))
    else:
        print("ERREUR file don't exist")

#The GUI

root = Tk()

#the MTGJSON Brand image
img = Image.open('img/MTGJSON-Brand-Assets/logo-mtgjson-black.png')
img=img.resize((50, 35))
img = ImageTk.PhotoImage(img)

#The entry for search the number of a card
E1 = Entry(root, bd=1,)

if E1.get()=="":
    E1.insert(0, "1")

#Output of all the information about the card
brand_text = Label(root,text="Powered by MTGJSON",)
brand = Label(root,image=img)
text = Label(root, text=card("10E",int(E1.get())),anchor='w',justify=LEFT)#using the fonction card()

# The Search Button
SearchButton = Button(root, text="Search", command=ButtonClick)

#The listbox that choose the set name
Lb1 = Listbox(root)
#Search all the file on json/
avalaible=os.listdir("json")
avalaible.sort()
#with all the name insert it in the list
for i in range(len(avalaible)):
    fi = avalaible[i][:len(avalaible[i])-5]
    Lb1.insert(i,fi)

#organisation of the windows

brand_text.grid(row=3,column=1,sticky="E")
brand.grid(row=3,column=2,sticky="SE")
E1.grid(row =1, column =1,sticky="WN")
text.grid(sticky="W",row =0, column =0,rowspan=3)
SearchButton.grid(row =2, column =1,sticky="WN")
Lb1.grid(row =0, column =1,sticky="WN")
#more config
root.wm_title("MTGCS")
root.geometry("720x640")
root.configure(bg='#5b5b5b')
root.mainloop()
