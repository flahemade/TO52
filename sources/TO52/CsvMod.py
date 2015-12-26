# coding: utf8
import csv;


__author__ = 'Iki'




class CsvMod :

    def __init__(self):
        print("New CsvMod")

    def buildCsv(self,nbPages,dico):
        c = csv.writer(open("MONFICHIER.csv", "wb"))
        entete  = list()
        entete.append("")
        entete.append("")
        for i in range(1,nbPages+1):
            string = i.__str__()
            string.encode('utf-8')
            entete.append(string)
        c.writerow(entete)

        for element in dico.keys():
            tmp=dico[element]
            previousAppearancePage=0

            #Reset currentLine
            currentLine=list()
            currentLine.append('')
            currentLine.append(element)

            currentWeight=1
            #Setting weight to 0



            ##print(element.__str__()+" : "+tmp.__str__())
            count=1

            for i in range(0,tmp.__len__()):
                entry=tmp[i]
                while(entry>count):
                    currentLine.append(0)
                    count+=1
                if(entry>previousAppearancePage):
                    #Next entry is after previous Appearance
                    previousAppearancePage=entry
                    #Reseting the weight
                    currentWeight=1
                elif(entry==previousAppearancePage):
                    #Same page than previous. Incrementing weight
                    currentWeight+=1
                elif(entry<previousAppearancePage):
                    #putting 0
                    currentLine.append(0)
                    previousAppearancePage+=1
                else:
                    print("Non tackled Exception")
                if(i+1==tmp.__len__()):
                    #Last appearance of entity
                    currentLine.append(currentWeight)
                    for j in range(0,nbPages-count):
                        currentLine.append(0)
                else:
                    if(tmp[i+1]>entry):
                        count+=1
                        currentLine.append(currentWeight)
                        currentWeight=1

            c.writerow(currentLine)
