import csv;


__author__ = 'Iki'




class CsvMod :

    def __init__(self):
        print("New CsvMod")

    def buildCsv(self,nbPages):
        c = csv.writer(open("MONFICHIER.csv", "wb"))
        entete  = list()
        entete.append("")
        for i in range(0,nbPages):
            entete.append(i.__str__())
        c.writerow(entete)


pouet = CsvMod()
pouet.buildCsv(32)