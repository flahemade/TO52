__author__ = 'Iki'

class Eval:

    def __init__(self):
        return

    def manualEvaluation(dico):
        bruit = 0
        silence = 0
        for line in dico :
            currentName = line[1]

            # On suppose que AskUser appelle une fonction d'affichage de ce nom
            # On suppose aussique cette fonction retourne un Bool�en

            if(AskUser(currentName)==False):

                # Ce personnage n'appara�t pas ou n'en est pas un

                bruit=bruit+1

        # On suppose que AskUser sans param�tre retourne une string si l'utilisateur saisit un nom

        while(AskUserForMissing()!=None):

            oubli=AskUserForMissing()
            silence = silence +1

        finalBruit = bruit / nbLine * 100
        finalSilence = silence / nbLine * 100

        print("Pour cette indexation, on a %s% de bruit et %s% de silence",finalBruit,finalSilence)

        return

    def AskUser(nameToAsk):
        #buildEvalInterface lance l'interface d'�valuation
        Gui.buildEvalInterface()
        #ask fait appara�tre ledit nom avec la possibilit� de r�pondre "oui" ou "non" et retourn un bool�en
        return Gui.ask(nameToAsk)

    def AskUserForMissing(self):
        #askForMissing fait appara�tre un champ texte et laisse la possibilit� entre Valider ou Terminer
        if(Gui.askForMissing()!=None):
            return Gui.askForMissing()

        return
