__author__ = 'Iki'

from tkFileDialog import askopenfilename
from Tkinter import *

def click(event):
            filepath = askopenfilename(title="Import a pdf",filetypes=[('pdf files','.pdf'),('all files','.*')])
            print filepath
            message2=Label(window,text=filepath)
            message2.pack()
            button_import.pack_forget()
            button_analyse=Button(window,text="Analyse")
            button_analyse.pack(side="bottom")

window = Tk()

button_import=Button(window,text="Import")
button_import.bind("<Button-1>",click)
button_import.pack(side="left")

window.mainloop()











