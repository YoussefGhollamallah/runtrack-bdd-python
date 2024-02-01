from db import *

class Produits(Db):
    def __init__(self, nom,description, prix, quantite, id_categorie):
        
        self.nom = nom
        self.description = description
        self.prix = prix
        self.quantite = quantite
        self.id_categorie = id_categorie

    def add_produit(self,produit):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO produits (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
            values = (produit.nom, produit.description, produit.prix, produit.quantite, produit.id_categorie)
            cursor.execute(query,values)
            self.connection.commit()
            cursor.close()
            print("produit ajoutée avec succès.")
        except mysql.connector.Error as err:
            print(f"erreur {err}")


mydb = Db(host='localhost', user="root",password="root",database="store")
# try:
#     mydb.connect()

#     test_add = Produits(nom="Pomme",description="Fruit récolté en espagne", prix=1.50,quantite=10,id_categorie=1)
#     mydb.add_produit(test_add)

# finally:
#     mydb.disconnect()