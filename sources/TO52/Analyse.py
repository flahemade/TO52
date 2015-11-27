from TO52.Parse import Parse
from TO52.Book import Book
from TO52.Perso import Perso
from TO52.CsvMod import CsvMod

__author__ = 'Iki'


class Analyse:
    not_perso = []
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
                word = word.replace("'","-")
                sub_word = word.split('-')
                for sword in sub_word:
                    if len(sword)>0:
                        if ((ord(sword[0])>=65) and (ord(sword[0])<=90)):
                            sword = sword.upper()
                            if((ord(sword[-1])>=33 and ord(sword[-1])<=64)):
                                    sword = sword[0:-1]

                            if not Analyse.not_perso.__contains__(sword):
                                if sword not in Analyse.perso.keys():
                                    Analyse.perso[sword] = [i]
                                else:

                                    Analyse.perso.get(sword).append(i)
                        else:
                            test = sword.upper()
                            if(Analyse.perso.has_key(test)):
                                del Analyse.perso[test]
                                Analyse.not_perso.append(test)
            ##print Analyse.perso.keys()
        c = CsvMod()
        c.buildCsv(book.pages.__len__(),Analyse.perso)
        print Analyse.not_perso




