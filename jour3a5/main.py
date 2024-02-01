from produit import *


mydb.connect()


describe = "SELECT * FROM produits;"
resultat = mydb.execute_query(describe)

for ligne in resultat:
    print(ligne)