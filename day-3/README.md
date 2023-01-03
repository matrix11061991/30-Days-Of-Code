# Créer une liste d'appréciation de bulletin en fonction des moyennes des notes :
Tout d'abord, vous devez décider des intervalles de moyennes de notes qui détermineront l'appréciation de chaque étudiant. Par exemple, vous pouvez décider que les étudiants qui ont une moyenne supérieure ou égale à 16 sur 20 auront une appréciation "très bien", ceux qui ont une moyenne supérieure ou égale à 14 et inférieure à 16 auront une appréciation "bien", etc.

Créez une liste vide qui servira à stocker les appréciations de chaque étudiant.

Pour chaque étudiant, calculez sa moyenne de notes et utilisez les intervalles que vous avez définis pour déterminer son appréciation. Ajoutez l'appréciation de l'étudiant à la liste.

Répétez l'étape 3 pour chaque étudiant de la classe.

Affichez la liste des appréciations une fois que vous avez traité tous les étudiants.

Code en Python qui illustre comment réaliser cette tâche :

```python
def get_appreciations(notes, appreciation_intervals):
    appreciations = []
    for student_notes in notes:
        student_average = sum(student_notes) / len(student_notes)
        student_appreciation = None
        for appreciation, interval in appreciation_intervals.items():
            if interval[0] <= student_average < interval[1]:
                student_appreciation = appreciation
                break
        appreciations.append(student_appreciation)
    return appreciations
```
L'utilisation de cette fonction est de la manière suivante :

```python
# Exemple d'utilisation de la fonction

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
appreciations = get_appreciations(notes, appreciation_intervals)
print(appreciations)
```
