from TO52.Analyse import Analyse
from tkFileDialog import askopenfilename
from Tkinter import *

__author__ = 'Iki'


class Gui:
    window=0
    button_import=Button
    filepath=""

    def __init__(self):
        print("Gui starting")
        window = Tk()
        button_import = Button(window, text="Import")
        button_import.bind("<Button-1>", Gui.importation)
        button_import.pack(side="left")
        window.mainloop()

    @staticmethod
    def importation(event):
        Gui.filepath = askopenfilename(title="Import a pdf", filetypes=[('pdf files', '.pdf'), ('all files', '.*')])
        message2 = Label(Gui.window, text=Gui.filepath)
        message2.pack()
        Gui.button_import.pack_forget
        button_analyse = Button(Gui.window, text="Analyse")
        button_analyse.bind("<Button-1>", Gui.analyzing)
        button_analyse.pack(side="bottom")

    @staticmethod
    def analyzing(event):
        print("In process")
        a = Analyse()
        a.run(Gui.filepath)
