# ------------------------------------------------------ #
# AesoQ - Programm zum Loesen quadratischer Gleichungen  #
# Erstellt von Julius Bittner 10.12.2014                 #
# Letztes Aenderungsdatum 05.01.15                       #
# ------------------------------------------------------ #

import tkinter as tk
import math
import os

# STARTING FUNCTION

def start():

    global root

    global d
    global e
    global f
    global rd
	
    root = tk.Tk()
    root.title("AesoQ")
    root.config(bg="yellow")
    root.geometry("293x185+100+100")

    tk.Label(root, text="AesoQ", fg="blue", bg="yellow", font="Georgia 18").grid(row=0, columnspan=2)
    tk.Label(root, text="ax² + bx + c", fg="blue", bg="yellow", font="Georgia 12").grid(row=1, columnspan=2)

    tk.Label(root, text="a",     bg="yellow", font="Georgia 12").grid(row=2)
    tk.Label(root, text="b (p)", bg="yellow", font="Georgia 12").grid(row=3)
    tk.Label(root, text="c (q)", bg="yellow", font="Georgia 12").grid(row=4)
    tk.Label(root, text="runden",bg="yellow", font="Georgia 12").grid(row=5)

    d = tk.Entry(root, font="\"Courier New\" 12")
    d.grid(row=2, column=1)
    
    e = tk.Entry(root, font="\"Courier New\" 12")
    e.grid(row=3, column=1)
    
    f = tk.Entry(root, font="\"Courier New\" 12")
    f.grid(row=4, column=1)

    rd = tk.Entry(root, font="\"Courier New\" 12")
    rd.grid(row=5, column=1)
	
    pqbut = tk.Button(root, text="pq-Formel", bg="lightgreen", font="Georgia 12")
    pqbut.bind("<Button>", lambda event:pqformel())
    pqbut.grid(row=6,column=0)

    abcbut = tk.Button(root, text="abc-Formel", bg="lightgreen", font="Georgia 12")
    abcbut.bind('<Button>', lambda event:mitternachtsformel())
    abcbut.grid(row=6,column=1)
    
    menu()

# LOGICAL FUNCTTIONS

def mitternachtsformel ():
    """
    Voraussetzung: Punkte für Mitternachtsformel als Integer angegeben
    Ergebnis: Anzahl x und x geliefert
    """
    try:
        a = float(d.get())
        b = float(e.get())
        c = float(f.get())
        r = int (rd.get())
    except:
        fehler(0)

    try:
        rdx = math.sqrt(b**2-4*a*c)
        if rdx == 0:
            answ = "Es gibt eine Lösung für x:\n" + str(round(-b / 2*a, r))
        else:
            x1 = round((-b - rdx)/2*a, r)
            x2 = round((-b + rdx)/2*a, r)
            answ = "Es gibt zwei Lösungen für x:\n1.  " + str(x1) + "\n2.  " + str(x2)
    except ValueError:
        answ = "Es gibt für x keine Lösung."
    #except:
    #    fehler(2)
    #    return
    
    answ += "\n\nÜbergebene Gleichung:\n0 = " + str(a) + "x² + " + str(b) + "x +" + str(c)
    answ += "\ngerundet auf " + str(r) + " Stellen"
    fenster(answ, "300x185+393+100")
    
def pqformel ():
    """
    Voraussetzung: Punkte für Mitternachtsformel als Integer angegeben
    Ergebnis: Anzahl x und x geliefert
    """
    try:
        p = float(e.get())
        q = float(f.get())
        r = int (rd.get())
    except:
        fehler(0)
        
    try:
        if math.sqrt((p/2)**2-q) == 0:
            answ = "Es gibt eine Lösung für x:\t" + str(round(-p/2, r))
        else:
            x1 = round(-p/2 - math.sqrt((p/2)**2-q), r)
            x2 = round(-p/2 + math.sqrt((p/2)**2-q), r)
            answ = "Es gibt zwei Lösungen für x:\n1. " + str(x1) + "\n2. " + str(x2)
    except ValueError:
        answ = "Es gibt für x keine Lösung."
    #except:
    #    fehler(2)
    #    return
    
    answ += "\n\nÜbergebene Gleichung:\n0 = x² + " + str(p) + "x + " + str(q)
    answ += "\ngerundet auf " + str(r) + " Stellen"
    fenster(answ, "300x185+393+100")
    
def fehler(meldung):
    """
    Voraussetzung: meldung ist int
    Ergebnis: gibt Fehler aus
    meldung 0: falscher Datentyp
    meldung 1: x-Werte gleich
    """
    meldungen = {0: "Bitte überall nur Fließkommazahlen\n(mit Punkt statt Komma) angeben!",
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

    hilfemenu = tk.Menu(menubar)
    hilfemenu.add_command(label="Hilfe",command=gui_hilfe)
    hilfemenu.add_command(label="Über",command=gui_ueber)
    
    menubar.add_cascade(label="Datei",menu=dateimenu)
    menubar.add_cascade(label="Hilfe",menu=hilfemenu)
    
    root.config(menu=menubar)

def fenster(text, geo="50x50"):
    fenster = tk.Tk()
    fenster.geometry(geo)
    fenster.config(bg="yellow")
    fenster.title("AesoQ")
    tk.Label(fenster, text=text, font = "Georgia 12", fg="blue", bg="yellow").pack()
    tk.Button(fenster, text="Schließen", bg="lightgreen", font="Georgia 12", command=fenster.destroy).pack()

def gui_hilfe():
    """
    zeigt Hilfefenster an
    """
    hilfe = """
    Die Gleichung muss vorher manuell in die Form 0 = ax² + bx + c gebracht werden.

    Danach muss die Zahl a in das Feld a eingegeben werden - als Fließkommazahl mit Punkt statt Komma, also beispielsweise eine Zahl im Format 3.5 .
    Sollte a = 1 sein, kann man das Feld a auch leer lassen.
    Genauso verfährt man mit den Variablen b und c. Sollte a = 1 sein, werden die Felder nachfolgend nicht mehr b,
    sondern p und q anstelle von c genannt.  0 = x² + px + q
    Dann muss in das Feld runden noch eine Zahl eingegeben werden, auf wie viele Stellen das Ergebnis gerundet werden soll.

    Diese Datei findet man auch als Text in der Hilfe über die Menüleiste. Eine Information zum Programm findet man im Punkt "Über" im Menü Hilfe.
    Man kann das Fenster entweder über das Schließkreuz oder über das Feld schließen im Menü Datei schließen.
    """
    fenster(hilfe, "1200x250")

def gui_ueber():
    """
    zeigt Über-Fenster an
    """
    fenster = tk.Tk()
    fenster.title("AesoQ")
    fenster.config(bg="yellow")
    fenster.geometry("300x234+400+120")
    tk.Label(fenster,
             font = "Georgia 12",
             bg="yellow",
             text = """
    AesoQ
    
    Copyright Julius Bittner 2015
    Version 0.1
    Release: 05.01.2015
    
    License: CC-BY 3.0\n""").pack()
    z = tk.Label(fenster, fg="darkred", font="Georgia 12", bg="yellow",
                 text = "Kontakt: content.legoag@gmail.com")
    z.bind("<Button>",
           lambda event:os.startfile("http://mailto:content.legoag@gmail.com"))
    z.pack()
    tk.Button(fenster, text="Schließen", bg="lightgreen", font="Georgia 12", command=fenster.destroy).pack()

start()
    
# ENDE

tk.mainloop()
