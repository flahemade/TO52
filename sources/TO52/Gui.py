from TO52.Analyse import Analyse

__author__ = 'Iki'

from tkFileDialog import askopenfilename
from Tkinter import *

def importation(event):
    filepath = askopenfilename(title="Import a pdf", filetypes=[('pdf files', '.pdf'), ('all files', '.*')])
    print filepath
    message2 = Label(window, text=filepath)
    message2.pack()
    button_import.pack_forget()
    button_analyse = Button(window, text="Analyse")
    button_analyse.bind("<Button-1>", analyzing)
    button_analyse.pack(side="bottom")


def analyzing(event):
    print("In process")
    a = Analyse()
    a.printout()


window = Tk()

button_import = Button(window, text="Import")
button_import.bind("<Button-1>", importation)
button_import.pack(side="left")

window.mainloop()
