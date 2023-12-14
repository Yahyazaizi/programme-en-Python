from abc import ABC, abstractmethod

class Composition:
    def __init__(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite

    @property
    def getproduit(self):
        return self.__produit

    @property
    def getquantite(self):
        return self.__quantite

    def produit(self, new_produit):
        self.__produit = new_produit

    def quantite(self, new_quantite):
        self.__quantite = new_quantite

    def __str__(self):
        return f"{self.__quantite} x {str(self.__produit)}"



class Produit(ABC):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def getnom(self):
        return self.__nom

    @property
    def getcode(self):
        return self.__code

    @abstractmethod
    def getPrixHT(self):
        pass




class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    def __str__(self):
        return f"{self.getnom} {str(self.getcode)}: {str(self.getPrixHT())} dh"

    def getPrixHT(self):
        return self.__prixAchat


class ProduitCompose(Produit):
    tauxTVA = 0.18

    def __init__(self, nom, code, fraisFabrication, listeConstituants):
        super().__init__(nom, code)
        self.__fraisFabrication = fraisFabrication
        self.__listeConstituants = listeConstituants

    @property
    def fraisFabrication(self):
        return self.__fraisFabrication

    @property
    def listeConstituants(self):
        return self.__listeConstituants

    def __str__(self):
        compositions_str = ", ".join(str(comp) for comp in self.__listeConstituants)
        return f"{self.getnom} ({str(self.getcode)}): {str(self.getPrixHT())}:{str(self.__fraisFabrication)}[{compositions_str}] dh"

    def getPrixHT(self):
        prix_ht_constituants = sum(comp.getproduit.getPrixHT() * comp.getquantite for comp in self.__listeConstituants)
        return prix_ht_constituants + self.__fraisFabrication





# Example 
p1 = ProduitElementaire("P1", "001", 10.0)
p2 = ProduitElementaire("P2", "002", 15.0)

composition_p3 = [Composition(p1, 2), Composition(p2, 4)]
composition_p4 = [Composition(p2, 3), Composition(p1, 2)]

p3 = ProduitCompose("P3", "003", 5.0, composition_p3)
p4 = ProduitCompose("P4", "004", 8.0, composition_p4)

print(p1)
print(p2)
print(p3)
print(p4)
