# -*- coding: utf-8 -*-
class Zdict(object):
    "" """docstring for Zdict"""

    def __init__(self):
        self.dictionnaire = {}

    def __repr__(self):
        if self.dictionnaire:
            return "{}".format(self.dictionnaire)
        else:
            return "vous n'avez pas de dico"

    def __getitem__(self, index):
        "" """ retourne la valeur de l'index entre par l'utilisateur dans son dico """
        return self.dictionnaire[index]

    def __setitem__(self, index, value):
        "" """ change la valeur de l'index entre dans son dico"""
        self.dictionnaire[index] = value
        print("{}".format(self.dictionnaire[index])) 

        