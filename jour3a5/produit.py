import mysql.connector
from db import *
from tkinter import *

class Produits(Db):
    def __init__(self, nom, description, prix, quantite, id_categorie):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.quantite = quantite
        self.id_categorie = id_categorie
        self.connection = None

    def connect(self):
       
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="store"
        )


    def disconnect(self):
        if self.connection:
            self.connection.close()

    def add_produit(self):
        try:
            if self.connection is None:
                raise ValueError("Database connection is not established.")

            cursor = self.connection.cursor()
            query = "INSERT INTO produits (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
            values = (self.nom, self.description, self.prix, self.quantite, self.id_categorie)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return "Produit ajouté avec succès."
        except mysql.connector.Error as err:
            print(f"Erreur: {err}")
                
    def delete_product_by_name(self, nom_produit):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM produits WHERE nom = %s"
            cursor.execute(query, (nom_produit,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de la suppression du produit : {str(e)}")
            return False

    def get_all_produits(self):
        try:
            if self.connection is None:
                self.connect()

            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM produits LEFT JOIN categories ON produits.id_categorie = categories.id"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print(f"Erreur lors de la récupération de tous les produits : {err}")
            return None
