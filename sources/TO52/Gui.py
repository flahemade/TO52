from TO52.Analyse import Analyse
from tkFileDialog import askopenfilename
from Tkinter import *

__author__ = 'Iki'


class Gui:

    window = 0
    button_import = Button
    button_analyse = Button
    button_eval = Button
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
        Gui.button_analyse = Button(Gui.window, text="Analyse")
        Gui.button_analyse.bind("<Button-1>",Gui.analyzing())
        Gui.button_analyse.pack(side="bottom")

    @staticmethod
    def analyzing():
        print("In process")
        a = Analyse()
        a.run(Gui.filepath)
        Gui.button_eval = Button(Gui.window, text="Evaluate")
        print("Uesh je fais le bouton t'as vu")
        Gui.button_eval.bind("<Button-1>", Gui.build_eval_interface)
        Gui.button_analyse.pack(side="bottom")

    @staticmethod
    def build_eval_interface():
        print("lol")

