# coding: utf8
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
        perso_tmp = {}
        print("Analyse : Calling parser")
        p = Parse()
        book = p.run(path)
        i = 0
        for page in book.pages:
            i += 1
            text = page.text

            if i == 78:
                print text
            words = text.split()
            words = words[0:-1]
            previous_word = " "
            for word in words:
                word = word.replace("'","-")
                sub_word = word.split('-')
                for sword in sub_word:
                    if len(sword)>0:
                        if ((ord(sword[0])>=65) and (ord(sword[0])<=90)):
                            sword.lower()
                            if i == 78 or i == 79:
                                print previous_word
                                print sword
                            if 33 <= ord(sword[-1]) <= 64:
                                    sword = sword[0:-1]

                            if not Analyse.not_perso.__contains__(sword):
                                if sword not in Analyse.perso.keys():
                                    if sword in perso_tmp.keys():
                                        perso_tmp.get(sword).append(i)
                                        if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-1] == '-') and (not previous_word[-1] == '"'):
                                            Analyse.perso[sword] = perso_tmp.get(sword)
                                            del perso_tmp[sword]
                                    else:
                                        if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-1] == '-') and (not previous_word[-1] == '"'):
                                            Analyse.perso[sword] = [i]
                                        else:
                                            perso_tmp[sword] = [i]
                                else:
                                    Analyse.perso.get(sword).append(i)
                        else:
                            sword = sword.upper()
                            if(Analyse.perso.has_key(sword)):
                                del Analyse.perso[sword]
                                Analyse.not_perso.append(sword)
                            if perso_tmp.has_key(sword):
                                del perso_tmp[sword]
                                Analyse.not_perso.append(sword)
                previous_word = word
            # print Analyse.perso.keys()
        for index in Analyse.perso.keys():
            occurence = Analyse.perso.get(index)
            if len(occurence) == 1:
                del Analyse.perso[index]
                Analyse.not_perso.append(index)

        c = CsvMod()
        c.buildCsv(book.pages.__len__(),Analyse.perso)




