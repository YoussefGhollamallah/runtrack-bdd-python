import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="laplateforme"
)

cursor = db.cursor()

cursor.execute("SELECT SUM(capacite) FROM salle")

resultat = cursor.fetchone()
personne = resultat[0]

print(f"La capacité de toutes les salles est de : {personne}")


cursor.close()
db.close()