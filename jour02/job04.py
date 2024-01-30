import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="laplateforme"
)

cursor = db.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

resultat = cursor.fetchall()

for nom, capacite in resultat:
    print(f"le nom de la salle est {nom} capacité de la salle : {capacite}")


cursor.close()
db.close()