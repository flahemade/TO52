# coding: utf8
from TO52.Analyse import Analyse
from tkFileDialog import askopenfilename
from Tkinter import *
from TO52.Eval import Eval
import csv

__author__ = 'Iki'


class Gui:

    window = ''
    button_import = Button(window, text="Import")
    button_analyse = Button(window, text="Analyse")
    button_eval = Button(window,text="Evaluate")
    secondColumn = StringVar(window)
    firstColumn = StringVar(window)


    def __init__(self):
        print("Gui starting")
        window = Tk()
        Gui.button_import.bind("<Button-1>", Gui.importation)
        Gui.button_import.pack(side="left")
        window.mainloop()

    @staticmethod
    def importation(e):
        Gui.filepath = askopenfilename(title="Import a pdf", filetypes=[('pdf files', '.pdf'), ('all files', '.*')])
        Gui.message = Label(Gui.window, text=Gui.filepath)
        Gui.message.pack()
        Gui.button_analyse.bind("<Button-1>", Gui.analyzing)
        Gui.button_analyse.pack(side="bottom")

    @staticmethod
    def analyzing(e):
        print("In process")
        a = Analyse()
        a.run(Gui.filepath)
        print("Normalement, la, je les defonce.")
        Gui.button_import.destroy()
        Gui.button_analyse.destroy()
        Gui.message.pack_forget()
        Gui.message = Label(Gui.window, text="Analyse completed, CSV has been generated.")
        Gui.message.pack()
        Gui.button_eval.bind("<Button-1>", Gui.build_eval_interface)
        Gui.button_eval.pack(side="bottom")

    @staticmethod
    def build_eval_interface(e):
        e = Eval()
        with open('MONFICHIER.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            Gui.toEval = list()
            for row in spamreader:
                if(row[1]!=""):
                    tmp=row[1]
                    tmp = re.sub("[[]", '', tmp)
                    tmp = re.sub("[]]", '', tmp)
                    tmp = re.sub("\"", '', tmp)
                    tmp = re.sub("'", '', tmp)
                    Gui.toEval.append(tmp)


            Gui.firstColumn.set("First") # default value
            first = apply(OptionMenu, (Gui.window, Gui.firstColumn) + tuple(Gui.toEval))
            first.pack(side="left")


            Gui.secondColumn.set("Second") # default value
            second = apply(OptionMenu, (Gui.window, Gui.secondColumn) + tuple(Gui.toEval))
            second.pack(side="right")

            Gui.button_eval.config(text='Associate')
            Gui.button_eval.unbind("<Button-1>")
            Gui.button_eval.bind("<Button-1>", Gui.associate)

    @staticmethod
    def associate(e):
        print("Associating \'"+Gui.firstColumn.get()+"\' and \'"+Gui.secondColumn.get()+"\'")
        print("Yolo")


