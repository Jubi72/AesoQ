# ------------------------------------------------------ #
# AesoQ - Programm zum Lösen quadratischer Gleichungen   #
# Erstellt von Julius Bittner 10.12.2014                 #
# Letztes Änderungsdatum 02.04.15                        #
# ------------------------------------------------------ #

import tkinter as tk
import math
import os

class Gui:

    def __init__(self):
        
        self.root = tk.Tk()

        self.root.title("AesoQ")
        self.root.config(bg="yellow")
        self.root.geometry("293x185+100+100")

        tk.Label(self.root, text="AesoQ", fg="blue", bg="yellow",
                 font="Georgia 18").grid(row=0, columnspan=2)
        tk.Label(self.root, text="ax² + bx + c", fg="blue", bg="yellow",
                 font="Georgia 12").grid(row=1, columnspan=2)

        tk.Label(self.root, text="a",     bg="yellow",
                 font="Georgia 12").grid(row=2)
        tk.Label(self.root, text="b", bg="yellow",
                 font="Georgia 12").grid(row=3)
        tk.Label(self.root, text="c", bg="yellow",
                 font="Georgia 12").grid(row=4)
        tk.Label(self.root, text="runden",bg="yellow",
                 font="Georgia 12").grid(row=5)

        self.a_ent = tk.Entry(self.root, font=("Courier New", 12))
        self.a_ent.insert(0, "1")
        self.a_ent.grid(row=2, column=1)
        
        self.b_ent = tk.Entry(self.root, font=("Courier New", 12))
        self.b_ent.insert(0, "0")
        self.b_ent.grid(row=3, column=1)
        
        self.c_ent = tk.Entry(self.root, font=("Courier New", 12))
        self.c_ent.insert(0, "0")
        self.c_ent.grid(row=4, column=1)

        self.rd_ent = tk.Entry(self.root, font=("Courier New", 12))
        self.rd_ent.insert(0, "2")
        self.rd_ent.grid(row=5, column=1)

        button = tk.Button(self.root, text="Berechnen", bg="lightgreen",
                           font = "Georgia 12")
        button.bind("<Button>", lambda event: self.berechnen())
        button.grid(row=6, columnspan=2)

        self.menu()

        self.root.mainloop()


    def menu(self):

        menubar = tk.Menu(self.root)

        dateimenu = tk.Menu(menubar)
        dateimenu.add_command(label="Berechnen", command=self.berechnen)
        dateimenu.add_command(label="Schließen", command=self.root.destroy)

        hilfemenu = tk.Menu(menubar)
        hilfemenu.add_command(label="Hilfe", command=self.gui_hilfe)
        hilfemenu.add_command(label="Über", command=self.gui_ueber)
        
        menubar.add_cascade(label="Datei", menu=dateimenu)
        menubar.add_cascade(label="Hilfe", menu=hilfemenu)

        self.root.config(menu=menubar)


    def fenster(self, text, title="AesoQ", geo="50x50"):

        fenster = tk.Tk()
        fenster.geometry(geo)
        fenster.config(bg="yellow")
        fenster.title(title)

        tk.Label(fenster, text=text, font="Georgia 12", fg="blue",
                 bg="yellow").pack()
        tk.Button(fenster, text="Schließen", bg="lightgreen", font="Georgia 12",
                  command=fenster.destroy).pack()

        fenster.mainloop()

    def fehler(self, meldung):
        """
        Voraussetzung: meldung ist int
        Ergebnis: gibt Fehler aus
        meldung 0: falscher Datentyp
        """
        meldungen = {0: "Bitte überall nur Fließkommazahlen angeben\n" +
                        "(mit Punkt statt Komma)"}
        if not meldung in meldungen.keys():
            self.fenster("Unbekannter Fehler:\nBitte dem Entwickler melden!")
        else:
            self.fenster(meldungen[meldung])


    def gui_hilfe(self):
        # zeigt Hilfe an
        hilfe = """
Die Gleichung muss vorher manuell in die Form 0 = ax² + bx + c gebracht werden.

Danach muss die Zahl a in das Feld a eingegeben werden - als Fließkommazahl mit Punkt statt Komma, also beispielsweise eine Zahl im Format 3.5 .
Sollte a = 1 sein, kann man das Feld a auch leer lassen.
Genauso verfährt man mit den Variablen b und c. Diese erhalten allerdings den Standardwert 0. Die Standardgleichung ist also 0 = x².
Dann muss in das Feld runden noch eine Zahl eingegeben werden, auf wie viele Stellen das Ergebnis gerundet werden soll.

Diese Datei findet man auch als Text in der Hilfe über die Menüleiste. Eine Information zum Programm findet man im Punkt „Über“ im Menü Hilfe.
Man kann das Programm entweder über das Schließkreuz oder über das Feld „Schließen“ im Dateimenü beenden."""
        self.fenster(hilfe, "AesoQ: Hilfe", "1200x250")

    def gui_ueber(self):
        # zeigt Über-Fenster an
        fenster = tk.Tk()
        fenster.title("AesoQ")
        fenster.config(bg="yellow")
        fenster.geometry("300x234+400+120")
        tk.Label(fenster, font = "Georgia 12", bg="yellow",
                 text = """AesoQ
    
Copyright Julius Bittner 2015
Version 0.2
Release: 02.04.2015
    
License: CC-BY 3.0\n""").pack()
        z = tk.Label(fenster, fg="darkred", font="Georgia 12", bg="yellow",
                     text = "Kontakt: content.legoag@gmail.com")
        z.bind("<Button>",
               lambda event:os.startfile("http://mailto:content.legoag@gmail.com"))
        z.pack()

        tk.Button(fenster, text="Schließen", bg="lightgreen", font="Georgia 12",
                  command=fenster.destroy).pack()

        fenster.mainloop()

    def berechnen(self):

        try:
            a = float(self.a_ent.get())
            b = float(self.b_ent.get())
            c = float(self.c_ent.get())
            r = int (self.rd_ent.get())
        except:
            fehler(0)
            return
        
        answ  = "\nÜbergebene Gleichung:\n0 = " + str(a)
        answ += "x² + " + str(b) + "x +" + str(c)
        answ += "\ngerundet auf " + str(r) + " Stellen\n\n"
    
        try:
            rdx = math.sqrt(b*b - 4*a*c)
        except ValueError:
            answ += "Es gibt für x keine Lösung.\n"
            self.fenster(answ, "AesoQ: Ergebnis", "300x185+393+100")
            return
        
        if rdx == 0:
            answ += "Es gibt eine Lösung für x:\n"
            answ += str(round(float(-b / (2*a)),r)) + "\n"
        else:
            x1 = round(float((-b - rdx)/(2*a)), r)
            x2 = round(float((-b + rdx)/(2*a)), r)
            xg = max(x1, x2)
            xk = min(x1, x2)
            answ += "Es gibt 2 Lösungen für x:\n1.  " + str(xk)
            answ += "\n2.  " + str(xg) + "\n"

        self.fenster(answ, "AesoQ: Ergebnis", "300x185+393+100")

gui = Gui()
