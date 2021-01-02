from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def showInfoUPDATE():
    messagebox.showinfo("SNOW-Client: Update-Center",
                        "Aktualisieren sie den SNOW-Client über GitHub, wo sie ihn her haben!")


def closeAll():
    messagebox.askyesno("SNOW-Client", "Wirklich beenden?")
    Fenster.destroy()

def InfoBox():
    messagebox.showinfo("SNOW-Client: Infostand", "Made by SNOW -> 2021 -> Version Alpha 0.2 ")

def AppNews():
    messagebox.showinfo("SNOW-Client: DEINE CHANCE", "Schick mir ein mit Python 3.8.5 gecodetes Programm ein und DU kommst MIT deinem Programm hier in dieses Menü: [Programmname] von [Dein GitHub Nutzername]")

def initMenu():
    Anwendungsmenu = Menu(Menuleiste, tearoff=0)
    Menuleiste.add_cascade(label="Anwendung", menu=Anwendungsmenu)
    Anwendungsmenu.add_command(label="Update der App", command=showInfoUPDATE)
    Anwendungsmenu.add_command(label="Ende", command=closeAll)
    Hilfemenu = Menu(Menuleiste, tearoff = 0)
    Menuleiste.add_cascade(label="Hilfe", menu=Hilfemenu)
    Hilfemenu.add_command(label="Info", command=InfoBox)
    Appmenu = Menu(Menuleiste, tearoff = 0)
    Menuleiste.add_cascade(label="Apps", menu=Appmenu)
    Appmenu.add_command(label="(Hier könnte DEIN Programm stehen! Klicke für mehr!)", command=AppNews)


Fenster = Tk()
Fenster.title("SNOW-Client")
Fenster.config(width=270, height=120)
Menuleiste = Menu(Fenster)
Fenster.config(menu=Menuleiste)
initMenu()


Fenster.mainloop()
