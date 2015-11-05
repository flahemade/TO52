from TO52.Parse import Parse

__author__ = 'Iki'


class Analyse:

    def __init__(self):
        print("Analyse")

    @staticmethod
    def printout():
        print('Print')

    @staticmethod
    def run(path):
        print("Analyse : Calling parser")
        p = Parse()
        p.run(path)
