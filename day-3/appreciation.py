# Liste des notes de chaque étudiant
notes = [[18, 15, 16, 17], [15, 14, 14, 14], [12, 13, 14, 15], [16, 16, 17, 18]]
# Intervalles de moyennes qui déterminent l'appréciation
appreciation_intervals = {
    "très bien": (16, 20),
    "bien": (14, 16),
    "assez bien": (12, 14),
    "moyen": (10, 12),
    "insuffisant": (0, 10)
}
# Liste vide qui servira à stocker les appréciations de chaque étudiant
appreciations = []
# Pour chaque étudiant
for student_notes in notes:
    # Calcul de la moyenne de notes de l'étudiant
    student_average = sum(student_notes) / len(student_notes)
    # Recherche de l'appréciation de l'étudiant en fonction de sa moyenne
    student_appreciation = None
    for appreciation, interval in appreciation_intervals.items():
        if interval[0] <= student_average < interval[1]:
            student_appreciation = appreciation
            break

    # Ajout de l'appréciation de l'étudiant à la liste
    appreciations.append(student_appreciation)

# Affichage de la liste des appréciations
print(appreciations)
