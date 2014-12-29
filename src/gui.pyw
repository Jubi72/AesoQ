# AesoQ-Datei fuer das Graphical User Interface (letzte Änderung 24.12.14)

import tkinter as tk
import servus

def start():

    global root
    global a
    global b
    global c
	
    root = tk.Tk()
    root.title("AesoQ")
    root.config(bg="yellow")

    tk.Label(root, text="AesoQ", fg="blue").grid(row=0, columnspan=2)

    tk.Label(root, text="a").grid(row=1)
    tk.Label(root, text="b (p)").grid(row=2)
    tk.Label(root, text="c (q)").grid(row=3)

    a = tk.Entry(root)
    a.grid(row=1, column=1)
    a.insert(0, "0")
    b = tk.Entry(root)
    b.grid(row=2, column=1)
    b.insert(0, "0")
    c = tk.Entry(root)
    c.grid(row=3, column=1)
    c.insert(0, "0")

    abcbut = tk.Button(root, text="abc-Formel", bg="lightgreen",
                       command=servus.mitternachtsformel( a.get(), b.get(), c.get() )
                       )
    abcbut.grid(row=4,column=0)
    abcbut.bind('<Control-a>',servus.mitternachtsformel (a.get(), b.get(), c.get()))
    pqbut  = tk.Button(root, text="pq-Formel", bg="lightgreen",
                       command=servus.pqformel( b.get(), c.get() )
                       )
    pqbut.grid(row=4,column=1)
    pqbut.bind('<Control-p>', servus.pqformel(b.get(), c.get()))
    menu()

def menu():

    menubar = tk.Menu(root)

    dateimenu = tk.Menu(menubar)
    dateimenu.add_command(label="Schließen",command=root.destroy)
    root.bind('<Control-w>', root.destroy)

    hilfemenu = tk.Menu(menubar)
    hilfemenu.add_command(label="Hilfe",command=servus.gui_hilfe)
    root.bind('<F1>',servus.gui_hilfe)
    hilfemenu.add_command(label="Über",command=servus.gui_ueber)
    root.bind('<F12>',servus.gui_ueber)
    
    menubar.add_cascade(label="Datei",menu=dateimenu)
    menubar.add_cascade(label="Hilfe",menu=hilfemenu)
    
    root.config(menu=menubar)

start()
    
# ENDE

tk.mainloop(6)
