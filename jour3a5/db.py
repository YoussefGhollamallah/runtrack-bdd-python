import mysql.connector

class Db:
    def __init__(self,host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password= self.password,
            database= self.database
        )

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
    
    def execute_query(self, query):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
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
    
