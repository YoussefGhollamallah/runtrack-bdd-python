import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="work"
)

cursor = db.cursor()

test = db.cursor()

cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
resultat = cursor.fetchall()

test.execute("SELECT * FROM employe INNER JOIN service ON employe.id_service = service.id;")
jointure = test.fetchall()

print()
# permet d'afficher les salaires au dessus de 3000 €
print("Voici la liste des salarié touchant plus de 3000 € :")
for i in resultat:
    print(f" - {i[2]} {i[1]} touche un salaire {i[3]} €.")

print()

print("Voici la liste des salariée :")
for j in jointure:
    print( f" - {j[2]} {j[1]} travaille au service {j[6]}.")


test.close()
cursor.close()
db.close()