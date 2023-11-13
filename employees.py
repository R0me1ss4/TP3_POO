class Employe:
    def __init__(self, nom, identifiant, pin=500):
        self.nom = nom
        self.id = identifiant
        self.pin = pin

    def calcul_prime(self, a):
        if a:
            return self.pin * 2
        else:
            return self.pin * 0.5

    def salaire(self, prime):
        return self.pin * prime

    def affiche(self, a):
        prime = self.calcul_prime(a)
        salaire_calcul = self.salaire(prime)

        print("Nom:", self.nom)
        print("ID:", self.id)
        print("Point indiciaire (Pin):", self.pin)
        print("Prime:", prime)
        print("Salaire:", salaire_calcul)
        print("Statut: Employé")
        
class Ingenieur(Employe):
    def __init__(self, nom, identifiant, etat, pin=500):
        super().__init__(nom, identifiant, pin)
        self.etat = etat

    def salaire2(self, prime):
        if self.etat == "stagiaire":
            return self.pin * 4 * prime
        else:
            return self.pin * 6 * prime

    def affiche2(self,a):
        prime = self.calcul_prime(a)  # Appel de la méthode calcul_prime de la classe Employe
        salaire_calcul = self.salaire2(prime)

        print("Nom:", self.nom)
        print("ID:", self.id)
        print("Point indiciaire (Pin):", self.pin)
        print("Prime:", prime)
        print("Salaire:", salaire_calcul)
        print("Statut: Ingénieur " + self.etat)

class Technicien(Employe):
    def __init__(self, nom, identifiant, pin=500):
        super().__init__(nom, identifiant, pin)

    def salaire3(self, prime):
        return self.pin * 2 * prime

    def affiche3(self,a):
        prime = self.calcul_prime(a)  # Appel de la méthode calcul_prime de la classe Employe
        salaire_calcul = self.salaire3(prime)

        print("Nom:", self.nom)
        print("ID:", self.id)
        print("Point indiciaire (Pin):", self.pin)
        print("Prime:", prime)
        print("Salaire:", salaire_calcul)
        print("Statut: Technicien")