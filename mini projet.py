
# bibliothèques
import random

# initialisation
nb_coups_max = 10
meilleur_score = 100
meilleur_prenom = "personne"

# début du programme
print("\n*************************")
print("**  Jeu du JUSTE PRIX  **")
print("*************************\n")
print("Devine un nombre entre 1 et 100")
print("Le programme te dira si tu as trouvé le nombre")
print("Ou s'il est plus petit ou plus grand\n")
reponse_rejouer = "oui"

while reponse_rejouer == "oui":
    # initialisation à chaque nouvelle partie
    nombre_a_trouver = random.randint(1,100)
    nombre_utilisateur = 0
    compteur = 0

    # début du programme pour une novelle partie
    prenom = input("Quel est ton prenom : ")
    while nombre_utilisateur != nombre_a_trouver and compteur < nb_coups_max:
        nombre_utilisateur = int(input("Saisir un nombre : "))
        compteur = compteur + 1
        if nombre_a_trouver < nombre_utilisateur:
            print("Le nombre à trouver est plus petit")
        else:
            print("Le nombre à trouver est plus grand")

    if nombre_utilisateur == nombre_a_trouver :
        print(f"Bravo {prenom}, tu as trouvé en {compteur} coups !")
        if compteur <= meilleur_score :
            print(f"Tu as un meilleur score que {meilleur_prenom} qui avait un score de {meilleur_score} coups")
            meilleur_score = compteur
            meilleur_prenom = prenom
        else:
            print(f"Tu n'as PAS battu le meilleur score de {meilleur_prenom} qui avait un score de {meilleur_score} coups")
    else:
        print("\n{prenom}, tu as perdu ! Nombre de coups max atteint !")
        print(f"Le nombre à trouver était {nombre_a_trouver}")
        print(f"Tu n'as PAS battu le meilleur score de {meilleur_prenom} qui avait un score de {meilleur_score} coups")

    reponse_rejouer = input("Veux-tu rejouer (oui/non) ? ")

print("A bientôt")

