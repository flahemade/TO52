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
                i=+1
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
                        for row2 in reader2:
                            name2 = row2[0]
                            set1 = set(name1.split(' '))
                            set2 = set(name2.split(' '))

                            for item1 in set1:
                                for item2 in set2:
                                    item2=item2.lower()
                                    if item1 == item2:
                                        if(listPerso.__len__()>1):
                                            if(listPerso[-1]!=name1):
                                                listPerso.append(name1)
                                        else:
                                            listPerso.append(name1)
    print(listPerso)
