# coding: utf8
from TO52.Parse import Parse
from TO52.Book import Book
from TO52.Perso import Perso
from TO52.CsvMod import CsvMod
from copy import deepcopy
from collections import Counter

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
                                if(65<=ord(previous_word[0])<=90) and (not previous_word[-1] == '.') and \
                                    (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and \
                                    (not previous_word[-3:] == '—') and (not previous_word[-3:] == '«') and \
                                    (not previous_word[-3:] == '…') and (not previous_word[-1] == ':') and \
                                    (not previous_word[-1] == ','):
                                    previous_word = Analyse.replace_spec(Analyse(),previous_word)
                                    previous_word = previous_word.lower()
                                    while(not ((65<=ord(previous_word[-1])<=90) or (97<=ord(previous_word[-1])<=122))):
                                        previous_word = previous_word[0:-1]
                                    if not Analyse.not_perso.__contains__(previous_word):
                                        if len(pers2.name) > 0:
                                            pers2.name = [pers2.name[0] + " " + sword]
                                        else:
                                            pers2.name = [previous_word + " " + sword]
                                        test_stop = 1
                                else:
                                    if len(pers2.name)>0:
                                        for pers in Analyse.perso.keys():
                                            if pers2.name[0] == pers.name[0]:
                                                Analyse.perso.get(pers).append(i)
                                                test_stop = 1
                                        if test_stop==0:
                                            for pers in perso_tmp.keys():
                                                if pers2.name[0] == pers.name[0]:
                                                    test_stop = 1
                                                    perso_tmp.get(pers).append(i)
                                                    if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-3:] == '—') and (not previous_word[-3:] == '«') and (not previous_word[-3:] == '…') and (not previous_word[-1] == ':'):
                                                        Analyse.perso[pers] = perso_tmp.get(pers)
                                                        del perso_tmp[pers]
                                        if test_stop==0:
                                            if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-3:] == '—') and (not previous_word[-3:] == '«') and (not previous_word[-3:] == '…') and (not previous_word[-1] == ':'):
                                                Analyse.perso[deepcopy(pers2)] = [i]
                                                test_stop = 1
                                            else:
                                                perso_tmp[deepcopy(pers2)] = [i]
                                                test_stop = 1
                                    pers2.name = []
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

                                    pers2.name = []
                    else:
                        test_stop = 0
                        if len(pers2.name)>0:
                            for pers in Analyse.perso.keys():
                                if pers2.name[0] == pers.name[0]:
                                    Analyse.perso.get(pers).append(i)
                                    test_stop = 1
                            if test_stop==0:
                                for pers in perso_tmp.keys():
                                    if pers2.name[0] == pers.name[0]:
                                        test_stop = 1
                                        perso_tmp.get(pers).append(i)
                                        if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-3:] == '—') and (not previous_word[-3:] == '«') and (not previous_word[-3:] == '…') and (not previous_word[-1] == ':'):
                                            Analyse.perso[pers] = perso_tmp.get(pers)
                                            del perso_tmp[pers]
                            if test_stop==0:
                                if (not previous_word[-1] == '.') and (not previous_word[-1] == '?') and (not previous_word[-1] == '!') and (not previous_word[-3:] == '—') and (not previous_word[-3:] == '«') and (not previous_word[-3:] == '…') and (not previous_word[-1] == ':'):
                                    Analyse.perso[deepcopy(pers2)] = [i]
                                else:
                                    perso_tmp[deepcopy(pers2)] = [i]
                        pers2.name = []
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
            name = index.name[0].split()
            x = len(name)
            if x>1:
                j=0
                for n in name:
                    if n in Analyse.not_perso:
                        del name[j]
                        j=j-1
                    j=j+1
                if not x == len(name):
                    name = ''.join(name)
                    for index2 in Analyse.perso.keys():
                        if name == index2.name[0]:
                            print name
                            true_perso = Analyse.perso.get(index)
                            true_perso = Analyse.perso.get(index)+Analyse.perso.get(index2)
                            true_perso.sort()
                            del Analyse.perso[index]
                            Analyse.perso[index2] = true_perso



        list = []
        for index in Analyse.perso.keys():
            name = index.name
            split = name[0].split()
            if not name == split:
                list = list + split
        count = Counter(list)
        print count
        for elem in count.keys():
            list_same_perso = []
            if count.get(elem) == 1:
                for index in Analyse.perso.keys():
                    name = ' '.join(index.name)
                    if elem == "tom":
                        print name
                    if name == elem or elem in name.split():
                        list_same_perso.append(index)
            if len(list_same_perso) > 1:
                true_perso = Analyse.perso.get(list_same_perso[0])
                for i in range(1,len(list_same_perso)):
                    true_perso = (true_perso + Analyse.perso.get(list_same_perso[i]))
                    true_perso.sort()
                    if len(list_same_perso[0].name[0])> len(list_same_perso[i].name[0]):
                        list_same_perso[0].name = list_same_perso[0].name + list_same_perso[i].name
                    else:
                        list_same_perso[0].name = list_same_perso[i].name + list_same_perso[0].name
                    del Analyse.perso[list_same_perso[i]]
                Analyse.perso[list_same_perso[0]] = true_perso

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
        spec = { 'A' : "À Á Â",
        'a' : "à á â",
        'Ae': "Æ",
        'ae' : "æ",
        'C' : "Ç",
        'c' : "ç",
        'E' : "È É Ê Ë",
        'e' : "è é ê ë",
        'I' : "Ì Í Î Ï",
        'i' : "ì í î ï",
        'N' : "Ñ",
        'n' : "ñ",
        'O' : "Ò Ó Ô",
        'o' : "ò ó ô",
        'Oe' : "Œ",
        'oe' : "œ",
        'U' : "Ù Ú Û Ü",
        'u' : "ù ú û ü",
        'Y' : "Ý Ÿ",
        'y' : "ý ÿ"}

        for key in spec.keys():
            chars = spec.get(key).split()
            for char in chars:
                word = word.replace(char,key)

        return word
