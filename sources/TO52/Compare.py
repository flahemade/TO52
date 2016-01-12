# coding: utf8
from Tkinter import *
import csv

__author__ = 'Iki'


class Compare:
    with open('MONFICHIER.csv', 'rb') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        i=0
        listPerso = list()
        for row1 in reader1:
                i=i+1
                with open('ender.csv', 'rb') as toCompare:
                    reader2 = csv.reader(toCompare, delimiter=',', quotechar='|')
                    name1 = row1[1]
                    if (name1 != ""):
                        tmp = name1
                        tmp = re.sub("[[]", '', tmp)
                        tmp = re.sub("[]]", '', tmp)
                        tmp = re.sub("\"", '', tmp)
                        tmp = re.sub("'", '', tmp)
                        name1 = tmp
                        j=0
                        for row2 in reader2:
                            j=j+1
                            name2 = row2[0]
                            set1 = set(name1.split(' '))
                            set2 = set(name2.split(' '))

                            for item1 in set1:
                                for item2 in set2:
                                    item2=item2.lower()
                                    if item1 == item2:
                                        if(listPerso.__len__()>1):
                                            toAppend=1
                                            for element in listPerso:
                                                if(element!=name2):
                                                    toAppend=0
                                                else:
                                                    toAppend=1
                                            if(toAppend<1):
                                                listPerso.append(name2)
                                        else:
                                            listPerso.append(name2)
    print(i)
    print(j)
    print("On détecte "+listPerso.__len__().__str__()+"/"+j.__str__()+" des personnages présents dans l'index manuel.")
    print("On détecte "+ (i-listPerso.__len__()).__str__() +" non pertinentes.")




