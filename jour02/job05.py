import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="laplateforme"
)

cursor = db.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")

resultat = cursor.fetchone()
superficie = resultat[0]

print(f"La superficie de la Plateforme est de {superficie} m2")


cursor.close()
db.close()