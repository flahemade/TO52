from TO52.Parse import Parse
from TO52.Book import Book
from TO52.Perso import Perso

__author__ = 'Iki'


class Analyse:

    perso = {}
    def __init__(self):
        print("Analyse")

    @staticmethod
    def printout():
        print('Print')
        perso={}

    @staticmethod
    def run(path):

        print("Analyse : Calling parser")
        p = Parse()
        book = p.run(path)
        i = 0
        for page in book.pages:
            i = i + 1
            text = page.text
            words = text.split()
            for word in words:
                if ((ord(word[0])>=65) and (ord(word[0])<=90)):
                    word = word.upper()
                    if((ord(word[-1])>=33 and ord(word[-1])<=64)):
                        word = word[0:-1]
                    if word not in Analyse.perso.keys():
                        Analyse.perso[word] = [i]
                    else:

                        Analyse.perso.get(word).append(i)
                else:
                    test = word.upper()
                    if(Analyse.perso.has_key(test)):
                        Analyse.perso.__delitem__(test)
        print Analyse.perso.keys()




