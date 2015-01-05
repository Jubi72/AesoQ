# ----------------------------------------------------- #
# AesoQ - Programm zum Loesen quadratischer Gleichungen #
# Erstellt von Julius Bittner 10.12.2014                #
# Letztes Aenderungsdatum 05.01.15                      #
# ------------------------------------------------------#

import tkinter as tk
import math

# STARTING FUNCTION

def start():

    global root
    global a
    global b
    global c
	
    root = tk.Tk()
    root.title("AesoQ")
    root.config(bg="yellow")

    tk.Label(root, text="AesoQ", fg="blue", bg="yellow").grid(row=0, columnspan=2)

    tk.Label(root, text="a",     bg="yellow").grid(row=1)
    tk.Label(root, text="b (p)", bg="yellow").grid(row=2)
    tk.Label(root, text="c (q)", bg="yellow").grid(row=3)

    a = int()
    b = int()
    c = int()

    d = tk.Entry(root, textvariable = a)
    d.grid(row=1, column=1)
    d.insert(0, "1")
    e = tk.Entry(root, textvariable = b)
    e.grid(row=2, column=1)
    e.insert(0, "1")
    f = tk.Entry(root, textvariable = c)
    f.grid(row=3, column=1)
    f.insert(0, "0")

    abcbut = tk.Button(root, text="abc-Formel", bg="lightgreen")
    abcbut.bind('<Button>', lambda event:mitternachtsformel (a, b, c))
    abcbut.grid(row=4,column=0)
    pqbut = tk.Button(root, text="pq-Formel", bg="lightgreen")
    pqbut.bind("<Button>", lambda event:pqformel(b,c))
    pqbut.grid(row=4,column=1)
	
    menu()

# LOGICAL FUNCTTIONS

def mitternachtsformel (a, b, c):
    """
    Voraussetzung: Punkte für Mitternachtsformel als Integer angegeben
    Ergebnis: Anzahl x und x geliefert
    """
    try:
        rdx = b**2-4*a*c
        if math.sqrt(rdx) == 0:
            fenster("Es gibt eine Lösung für x:\t" + str(-b / 2*a))
        else:
            x1 = (-b - math.sqrt(rdx))/2*a
            x2 = (-b + math.sqrt(rdx))/2*a
            fenster("Es gibt zwei Lösungen für x:\n1. " + x1 + "\n2. " + x2)
    except ValueError:
        fenster("Es gibt für x keine Lösung.")
    except:
        fehler(2)
    
def pqformel (p, q):
    """
    Voraussetzung: Punkte für Mitternachtsformel als Integer angegeben
    Ergebnis: Anzahl x und x geliefert
    """
    try:
        if math.sqrt((p/2)**2-q) == 0:
            fenster("Es gibt eine Lösung für x:\t" + str(-p/2))
        else:
            x1 = -p/2 - math.sqrt((p/2)**2-q)
            x2 = -p/2 + math.sqrt((p/2)**2-q)
            fenster("Es gibt zwei Lösungen für x:\n1. " + x1 + "\n2. " + x2)
    except ValueError:
        fenster("Es gibt für x keine Lösung.")
    except:
        fehler(2)
    
def fehler(meldung):
    """
    Voraussetzung: meldung ist int
    Ergebnis: gibt Fehler aus
    meldung 0: falscher Datentyp
    meldung 1: x-Werte gleich
    """
    meldungen = {0: "Bitte eine Ganzzahl eingeben!",
                 1: "In einer Funktion kann jedem x-Wert nur genau ein y-Wert zugeordnet werden. " +
                 "Dies wurde hier nicht beachtet. Bitte ändern"
                 }
    if not meldung in meldungen.keys():
        fenster("Unbekannter Fehler. Bitte dem Entwickler melden!")
    else:
        fenster(meldungen[meldung])

# GUI FUNCTIONS

def menu():

    menubar = tk.Menu(root)

    dateimenu = tk.Menu(menubar)
    dateimenu.add_command(label="Schließen",command=root.destroy)
    root.bind('<Control-w>', root.destroy)

    hilfemenu = tk.Menu(menubar)
    hilfemenu.add_command(label="Hilfe",command=gui_hilfe)
    root.bind('<F1>',gui_hilfe)
    hilfemenu.add_command(label="Über",command=gui_ueber)
    root.bind('<F12>',gui_ueber)
    
    menubar.add_cascade(label="Datei",menu=dateimenu)
    menubar.add_cascade(label="Hilfe",menu=hilfemenu)
    
    root.config(menu=menubar)

def fenster(text):
    fenster = tk.Tk()
    fenster.title("AesoQ")
    tk.Label(fenster, text=text).pack()
    tk.Button(fenster, text="Schließen", command=fenster.destroy).pack()

def gui_hilfe():
    """
    zeigt Hilfefenster an
    """
    f = open("../readme.txt",mode="r")
    l = f.readlines()
    t = str()
    for elem in l:
        t += elem + "\n"
    f.close()
    h = tk.Tk()
    h.title("AesoQ - Über")
    g = tk.Text(h, height=20, width=50)
    g.insert("end", t)
    g.pack()
    tk.Button(fenster, text="Schließen", command=h.destroy).pack()

def gui_ueber():
    """
    zeigt Über-Fenster an
    """
    ueber = """
    AesoQ

    Copyright Julius Bittner 2015
    Version 0.1
	Release: 05.01.2015

    License: CC-BY 3.0
    """
    fenster(ueber)

start()
    
# ENDE

tk.mainloop()
