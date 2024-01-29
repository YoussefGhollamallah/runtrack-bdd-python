-- premiere version / compte le nombre d'étudiant grâce à la méthode count()
SELECT COUNT(*) FROM etudiants;

-- deuxièeme version / compte le nombre d'étudiant grâce à la function count() en donnant le nom nombre_etudiants à la table
SELECT COUNT(*) AS nombre_etudiants FROM etudiants;