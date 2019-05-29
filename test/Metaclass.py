#! usr/bin/python3.6
# -*- coding:utf-8 -*-

trace_classes = {}  # Notre dictionnaire vide


class MetaWidget(type):

    "" """Notre métaclasse pour nos Widgets.
    
    Elle hérite de type, puisque c'est une métaclasse.
    Elle va écrire dans le dictionnaire trace_classes à chaque fois
    qu'une classe sera créée, utilisant cette métaclasse naturellement."""

    def __init__(cls, nom, bases, dict):
        "" """Constructeur de notre métaclasse, appelé quand on crée une classe."""
        type.__init__(cls, nom, bases, dict)
        trace_classes[nom] = cls
        print(bases)
        print(dict)


class Widget(metaclass=MetaWidget):
	"" """ classe mere de la classe widget"""
	pass


class Button(Widget):
	"" """ classe definissant le boutton widget """
	pass

print(trace_classes)    