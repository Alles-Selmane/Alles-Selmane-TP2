'''EXERCICE-1'''
import json
import csv

# Lire le fichier JSON
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Ouvrir le fichier CSV en mode écriture
with open('data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Écrire l'en-tête du CSV
    csv_writer.writerow(['reel', 'imaginaire'])

    # Écrire les nombres complexes dans le fichier CSV
    for complexe in data:
        csv_writer.writerow(complexe)

print("Les nombres complexes ont été écrits dans data.csv")
'''EXERCICE-2'''
import csv

def charger_pokemons_csv(nom_fichier):
    pokemons = {}
    with open(nom_fichier, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Le nom du Pokémon est le premier élément de la ligne
            nom = row[0]
            # Les stats sont les éléments suivants, convertis en entiers
            stats = list(map(int, row[1:]))
            # Ajouter au dictionnaire
            pokemons[nom] = stats
    return pokemons

# Exemple d'utilisation
pkmn = charger_pokemons_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f'{nom}: {stats}')

# Tests
print(isinstance(pkmn, dict)) # True
print(isinstance(pkmn["Pikachu"], list)) # True
print(isinstance(pkmn["Pikachu"][0], int)) # True
