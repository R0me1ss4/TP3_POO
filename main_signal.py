from signal_module import Aleatoire, Deterministe, Addition

# Création d'un objet Aléatoire
aleatoire1 = Aleatoire(20, 2, 5)
aleatoire1.Init_Alea()

# Création d'un objet Déterministe
deterministe1 = Deterministe(20, 3)
deterministe1.valeurs()

# Appel des méthodes pour chaque classe
print("Aléatoire - Nombre d'échantillons:", aleatoire1.nbr)
print("Aléatoire - Moyenne:", aleatoire1.correlation())
aleatoire1.display()

print("Déterministe - Nombre d'échantillons:", deterministe1.nbr)
print("Déterministe - Moyenne:", deterministe1.correlation())
deterministe1.display()

# Appel de la fonction Addition
resultat_addition = Addition(aleatoire1, deterministe1)

# Plot des vecteurs tab de tous les objets
print("Aléatoire + Déterministe - Nombre d'échantillons:", resultat_addition.nbr)
print("Aléatoire + Déterministe - Moyenne:", resultat_addition.correlation())
resultat_addition.display()