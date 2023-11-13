import matplotlib.pyplot as plt
import numpy as np

class Signal:
    def __init__(self, nbr,tab):
        self.nbr = nbr
        self.tab = tab

    def echantillons(self):
        return self.nbr

    def moyenne(self):
        return np.mean(self.tab)

    def correlation(self):
        return np.corrcoef(self.tab[:-1], self.tab[1:])[0, 1]

    def display(self):
        print("Nombre d'échantillons:", self.nbr)
        print("Vecteur (tab):", self.tab)
        
        # Plot
        plt.stem(self.tab)
        plt.title("Graphique du Signal")
        plt.xlabel("Échantillons")
        plt.ylabel("Valeurs")
        plt.show()

class Aleatoire(Signal):
    def __init__(self, nbr, sigma, mean):
        super().__init__(nbr, np.zeros(nbr))  # Initialise le tableau tab avec des zéros
        self.sigma = sigma
        self.mean = mean

    def Init_Alea(self):
        self.tab = self.sigma * np.random.randn(self.nbr) + self.mean

    def correlation2(self):
        power_tab = np.power(self.tab, 2)
        print("Nom de la classe:", self.__class__.__name__)
        return power_tab

class Deterministe(Signal):
    def __init__(self, nbr, amplitude):
        super().__init__(nbr, np.zeros(nbr))
        self.amplitude = amplitude

    def valeurs(self):
        self.tab[:self.nbr//2] = self.amplitude
        self.tab[self.nbr//2:] = -self.amplitude

def Addition(aleatoire, deterministe):
    # Création d'un nouvel objet Déterministe
    S = Deterministe(max(aleatoire.nbr, deterministe.nbr), 0)
    
    # Somme des attributs tab des objets reçus en arguments
    S.tab[:aleatoire.nbr] += aleatoire.tab
    S.tab[:deterministe.nbr] += deterministe.tab
    
    return S