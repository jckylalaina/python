#!/usr/bin/python3
# -*- coding: utf-8 -*-
import psycopg2
import os
from psycopg2 import Error
from MVC.loading import *

try:

    # connct to database

    connection = psycopg2.connect(
        user="admin", password="root", host="127.0.0.1", port="5432", database="mydb"
    )
    cursor = connection.cursor()

    def save(nom, prenom):

        # inserion de nom et prenom dans la table utilisateur

        save = """ INSERT INTO utilisateur 
        (nom,prenom) VALUES (%s,%s) """
        print("\nentrain de sauvegarder")
        loading("sauvegarder")

        # executiion de la commande sql

        cursor.execute(save, (nom, prenom))
        print("sauvegarde reussie")

    def show_all():
        show = """ select * from utilisateur """
        result = cursor.execute(show)

        # transforme le resultat en tableau

        result = cursor.fetchall()
        return result

    def update(id, nom, prenom):
        update = """ update utilisateur set nom=%s , 
        prenom=%s where id=%s"""
        loading("mis a niveau")
        cursor.execute(update, (nom, prenom, id))
        print("mis a jour fait")

    def delete(id):
        delete = """ delete from utilisateur where id=%s """
        loading()
        cursor.execute(delete, (id,))
        print("*fait*")

    def show(id):
        show = """ select * from utilisateur where id=%s"""
        cursor.execute(show, id)
        result = cursor.fetchall()
        return result

    os.system("black app/models/user.py")
except:
    print("erreur")
