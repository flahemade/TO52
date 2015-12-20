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
        not_perso = []
        perso = {}

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
            words = text.split()
            words = words[0:-1]
            previous_word = "."
            for word in words:
                word = word.replace("'","-")
                sub_word = word.split('-')
                for sword in sub_word:
                    if len(sword)>1:
                        sword = Analyse.replace_spec(Analyse(),sword)
                        if ((ord(sword[0])>=65) and (ord(sword[0])<=90)):
                            sword = sword.lower()
                            while(not ((65<=ord(sword[-1])<=90) or (97<=ord(sword[-1])<=122))):
                                sword = sword[0:-1]
                            if len(sword)>1:
                                if not Analyse.not_perso.__contains__(sword):
                                    if sword not in Analyse.perso.keys():
                                        if sword in perso_tmp.keys():
                                            perso_tmp.get(sword).append(i)
                                            if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-3:] == '—') and (not previous_word[-3:] == '«') and (not previous_word[-3:] == '…') and (not previous_word[-1] == ':'):
                                                Analyse.perso[sword] = perso_tmp.get(sword)
                                                del perso_tmp[sword]
                                        else:
                                            if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-3:] == '—') and (not previous_word[-3:] == '«') and (not previous_word[-3:] == '…') and (not previous_word[-1] == ':'):
                                                Analyse.perso[sword] = [i]
                                            else:
                                                perso_tmp[sword] = [i]
                                    else:
                                        Analyse.perso.get(sword).append(i)
                        else:
                            sword = sword.lower()
                            if not (sword in Analyse.not_perso):
                                Analyse.not_perso.append(sword)
                            if(Analyse.perso.has_key(sword)):
                                del Analyse.perso[sword]
                            if perso_tmp.has_key(sword):
                                del perso_tmp[sword]
                previous_word = word
        for index in Analyse.perso.keys():
            occurence = []
            [occurence.append(item) for item in Analyse.perso.get(index) if item not in occurence]
            if len(occurence) == 1:
                del Analyse.perso[index]
                if not (index in Analyse.not_perso):
                    Analyse.not_perso.append(index)
        print len(Analyse.not_perso)
        c = CsvMod()
        c.buildCsv(book.pages.__len__(),Analyse.perso)

    def replace_spec(self,word):
        spec = {'a': "À Á Â à á â",
        'ae' : "Æ æ",
        'c' : "Ç ç",
        'e' : "È É Ê Ë è é ê ë",
        'i' : "Ì Í Î Ï ì í î ï",
        'n' : "Ñ ñ",
        'o' : "Ò Ó Ô ò ó ô",
        'oe' : "Œ œ",
        'u' : "Ù Ú Û Ü ù ú û ü",
        'y' : "Ý Ÿ ý ÿ"}

        for key in spec.keys():
            chars = spec.get(key).split()
            for char in chars:
                word = word.replace(char,key)

        return word
