# coding: utf8
from TO52.Parse import Parse
from TO52.Book import Book
from TO52.Perso import Perso
from TO52.CsvMod import CsvMod
from copy import deepcopy

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
        previous_word = "."
        for page in book.pages:
            i += 1
            text = page.text
            words = text.split()
            words = words[0:-1]
            pers2 = Perso([])
            for word in words:
                sword = word
                if len(sword)>1:
                    sword = Analyse.replace_spec(Analyse(),sword)
                    analyse_keys = Analyse.perso.keys()
                    tmp_keys = perso_tmp.keys()
                    if ((ord(sword[0])>=65) and (ord(sword[0])<=90)):
                        sword = sword.lower()
                        while(not ((65<=ord(sword[-1])<=90) or (97<=ord(sword[-1])<=122))):
                            sword = sword[0:-1]
                        if len(sword)>1:
                            test_stop = 0
                            if not Analyse.not_perso.__contains__(sword):
                                # if (65<=ord(previous_word[0])<=90):
                                #     previous_word = Analyse.replace_spec(Analyse(),previous_word)
                                #     previous_word = previous_word.lower()
                                #     while(not ((65<=ord(previous_word[-1])<=90) or (97<=ord(previous_word[-1])<=122))):
                                #         previous_word = previous_word[0:-1]
                                #     concat = previous_word +" "+ sword
                                #     test_pers_final = 0
                                #     test_pers_delete = 0
                                #     new_name = []
                                #     for pers in analyse_keys:
                                #         if test_pers_final == 0:
                                #             if previous_word in pers.name:
                                #                 pers_final = deepcopy(pers)
                                #                 Analyse.perso[pers].append(i)
                                #                 pers_final.name.append([concat,concat.split()])
                                #                 test_pers_final = 1
                                #         if test_pers_delete == 0:
                                #             if sword in pers.name:
                                #                 pers_delete = deepcopy(pers)
                                #                 l = Analyse.perso.get(pers)
                                #                 new_name = pers_delete.name
                                #                 del Analyse.perso[pers]
                                #                 test_pers_delete = 1
                                #     for pers in tmp_keys:
                                #         if test_pers_final == 0:
                                #             if previous_word in pers.name:
                                #                 pers_final = deepcopy(pers)
                                #                 perso_tmp[pers].append(i)
                                #                 pers_final.name.append([concat,concat.split()])
                                #                 test_pers_final = -1
                                #         if test_pers_delete == 0:
                                #             if sword in pers.name:
                                #                 pers_delete = deepcopy(pers)
                                #                 l = perso_tmp[pers]
                                #                 new_name = pers_delete.name
                                #                 del perso_tmp[pers]
                                #                 test_pers_delete = -1
                                #     pers_final.name.append(new_name)
                                #     test_stop=1
                                if test_stop==0:
                                    for pers in analyse_keys:
                                        if sword in pers.name:
                                            Analyse.perso.get(pers).append(i)
                                            test_stop = 1
                                if test_stop==0:
                                    for pers in tmp_keys:
                                        if sword in pers.name:
                                            test_stop = 1
                                            perso_tmp.get(pers).append(i)
                                            if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-3:] == '—') and (not previous_word[-3:] == '«') and (not previous_word[-3:] == '…') and (not previous_word[-1] == ':'):
                                                Analyse.perso[pers] = perso_tmp.get(pers)
                                                del perso_tmp[pers]
                                if test_stop==0:
                                    pers2.name = []
                                    pers2.name.append(sword)
                                    if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-3:] == '—') and (not previous_word[-3:] == '«') and (not previous_word[-3:] == '…') and (not previous_word[-1] == ':'):
                                        Analyse.perso[deepcopy(pers2)] = [i]
                                    else:
                                        perso_tmp[deepcopy(pers2)] = [i]
                    else:
                        sword = sword.lower()
                        sword = Analyse.replace_spec(Analyse(),sword)
                        if not (sword in Analyse.not_perso):
                            Analyse.not_perso.append(sword)
                        for pers in analyse_keys:
                            if sword in pers.name:
                                Analyse.not_perso.append(pers.name)
                                del Analyse.perso[pers]
                        for pers in tmp_keys:
                            if sword in pers.name:
                                Analyse.not_perso.append(pers.name)
                                del perso_tmp[pers]
                previous_word = word
        for index in Analyse.perso.keys():
            occurence = []
            [occurence.append(item) for item in Analyse.perso.get(index) if item not in occurence]
            if len(occurence) == 1:
                del Analyse.perso[index]
                if not (index in Analyse.not_perso):
                    Analyse.not_perso.append(index)
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
