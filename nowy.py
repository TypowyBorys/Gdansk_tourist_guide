import tkinter
import time
import sys

okno = tkinter.Tk()

def koniec():
    sys.exit()

l = tkinter.Label(okno, text= "Przykłądowy test")
b = tkinter.Button(okno, text = "Zakończ", command = koniec)


l.pack()
b.pack()


okno.mainloop()