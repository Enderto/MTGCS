from tkinter import *
import json
from pathlib import Path
import os
from PIL import Image, ImageTk



avalaible=os.listdir("json")
avalaible.sort()



def fileok(path):
    files = Path(path)
    if files.is_file():
        return True
    else:
        return False

sets = "M21"

x = open("json/"+sets+".json","r")
j = json.load(x)

bob=j["data"]["cards"][0]["name"]

def re(a):
    tmp = len(a)
    stmp = a.split()
    if (tmp >5):
        for i in range(5,len(stmp),5):
            stmp.insert(i,"\n")
        fs = ' '.join(stmp)
    else:
        fs = a
    return fs

def card(a,b):
    x = open("json/"+a+".json","r")
    j = json.load(x)
    out=""
    type = j["data"]["cards"][b]["types"][0]
    #debut carte
    out = out + "Name :\n"

    out = out + j["data"]["cards"][b]["name"]
    if (type!="Creature"):
        print("hey"+type)
    else:
        out = out+"\n------------------------------\nMana cost :\n"+j["data"]["cards"][b]["manaCost"]+"\n"
        
    out = out + "------------------------------\n"
    out = out + "Type :\n" + j["data"]["cards"][b]["originalType"]+"\n------------------------------\nSet code:\n"+j["data"]["cards"][b]["setCode"]+"\n"
    out = out + "------------------------------\n"
    out = out + "Description :\n" + re(j["data"]["cards"][b]["originalText"])+"\n"
    if (type=="Creature"):
        out = out + "------------------------------\nPower: \n"+j["data"]["cards"][b]["power"]+" / "+j["data"]["cards"][b]["toughness"]+"\n------------------------------\n"
    elif (type=="Planeswalker"):
        out = out + "-----------------------"+j["data"]["cards"][b]["loyalty"]+"-\n"
    out = out + "artist :\n" + j["data"]["cards"][b]["artist"]+"\n------------------------------\nnb from the set :\n"+str(j["data"]["cards"][b]["number"])+"/"+str(j["data"]["baseSetSize"])+"\n"
    #fin
    return out


def ButtonClick():
    for i in Lb1.curselection():
        choice=Lb1.get(i)

    if fileok("json/"+choice+".json")==True:
        text['text']=card(choice,int(E1.get()))
    else:
        print("ERREUR file don't exist")



root = Tk()

img = Image.open('img/MTGJSON-Brand-Assets/logo-mtgjson-black.png')
img=img.resize((50, 35))
img = ImageTk.PhotoImage(img)

E1 = Entry(root, bd=1,)

if E1.get()=="":
    E1.insert(0, "0")
print(E1.get())

brand_text = Label(root,text="Powered by MTGJSON",)
brand = Label(root,image=img)
text = Label(root, text=card("10E",int(E1.get())),anchor='w',justify=LEFT)


# create button, link it to clickExitButton()
exitButton = Button(root, text="Replace me!", command=ButtonClick)


Lb1 = Listbox(root)

for i in range(len(avalaible)):
    fi = avalaible[i][:len(avalaible[i])-5]
    Lb1.insert(i,fi)

#organise
brand_text.grid(row=3,column=1,sticky="E")
brand.grid(row=3,column=2,sticky="SE")
E1.grid(row =1, column =1,sticky="WN")
text.grid(sticky="W",row =0, column =0,rowspan=3)
exitButton.grid(row =2, column =1,sticky="WN")
Lb1.grid(row =0, column =1,sticky="WN")

root.wm_title("Tkinter window")
root.geometry("720x640")
root.configure(bg='#5b5b5b')
root.mainloop()