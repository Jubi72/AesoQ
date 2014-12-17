# AesoQ - Datei für Funktionen

import math
import tkinter as tk

def normalform_punkte (punkte):
    """
    Voraussetzung: 3 Punkte [[x1,y1],[x2,y2],[x3,y3]] als int angegeben, x-Werte nicht gleich
    Ergebnis: Parabel als Liste in Normalform geliefert
    """
    # TODO: fertigzustellen!
    for elem in punkte:
        for el in elem:
            if type(el) != int: fehler(0)
    if punkte[0][0] in (punkte[1][0],punkte[2][0]) or punkte[1][0] == punkte[2][0]:
        fehler(1)
    return [a, b, c]
    

def scheitelpunktform_punkte (punkte):
    """
    Voraussetzung: 3 Punkte [[x1,y1],[x2,y2],[x3,y3]] angegeben
    Ergebnis: Parabel als Liste in Scheitelpunktform geliefert
    """
    pass
    # return [a, d, e]

def normalform_scheitelpunktform(a, d, e):
    """
    Voraussetzung: Scheitelpunktform a(x+d)²+e gegeben
    Ergebnis: Normalform (a, b, c) geliefert
    """
    pass
    # return [a, b, c]

def scheitelpunktform_normalform(a, b, c):
    """
    Voraussetzung: Normalform ax²+bx+c gegeben
    Ergebnis: Scheitelpunktform (a, d, e) geliefert
    """
    pass
    # return [a, d, e]

def mitternachtsformel (a, b, c):
    """
    Voraussetzung: Punkte für Mitternachtsformel als Integer angegeben
    Ergebnis: Anzahl x und x geliefert
    """
    if type(a) == int and type(b) == int and type(c) == int:
        try:
            rdx = b**2-4*a*c
            if math.sqrt(rdx) == 0:
                return [1, -b / 2*a]
            else:
                return [2, [(-b - math.sqrt(rdx))/2*a, (-b + math.sqrt(rdx))/2*a]]
        except ValueError:
            return [0, None]
    else:
        fehler(0)

def pqformel (p, q):
    """
    Voraussetzung: Punkte für Mitternachtsformel als Integer angegeben
    Ergebnis: Anzahl x und x geliefert
    """
    if type(p) == int and type(q) == int:
        try:
            if math.sqrt((p/2)**2-q) == 0:
                return [1, -p/2]
                fenster("Es gibt eine Lösung für x:\t" + str(-p/2))
            else:
                x1 = -p/2 - math.sqrt((p/2)**2-q)
                x2 = -p/2 + math.sqrt((p/2)**2-q)
                return [2, [x1, x2]]
                fenster("Es gibt zwei Lösungen für x:\n1. " + x1 + "\n2. " + x2)
        except ValueError:
            return [0, None]
    else:
        fehler(0)
 
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
                   
# GUI-FUNKTIONEN
                   
def fenster(text):
    fenster = tk.Tk()
    fenster.title("Fehler")
    tk.Label(fenster, text=text).pack()
    tk.Button(fenster, text="Schließen", command=fenster.destroy).pack()
    
def gui_hilfe():
    """
    zeigt Hilfefenster an
    """
    # INCLUDE README
    fenster("(include readme)")
    
def gui_ueber():
    """
    zeigt Über-Fenster an
    """
    # ÜBERSEITE
    fenster("(Über-Seite)")