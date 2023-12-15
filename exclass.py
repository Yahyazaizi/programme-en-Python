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

    def setproduit(self, new_produit):
        self.__produit = new_produit

    def setquantite(self, new_quantite):
        self.__quantite = new_quantite

    def __str__(self):
        return f"{self.__quantite} :{str(self.__produit)}"
    
    def __eq__(self,a)  :
        return self.__produit==a.getproduit and self.__quantite==a.getquantite
        




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

    def __str__(self):
        return f"{self.getnom} {str(self.getcode)}: "
    def __eq__(self,a)  :
        return self.__nom==a.getnom and self.__code==a.getcode
    
     
class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    def __str__(self):
        return f"{self.getnom} {str(self.getcode)}: {str(self.getPrixHT())} dh"
    
    def getPrixHT(self):
        return self.__prixAchat
    
    def setPrixHT (self,n):
        self.__PrixHT=n


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





# Example usage
cpu = ProduitElementaire("cpu", "1", 1010)
ram = ProduitElementaire("ram", "2", 600)


composition_p4 = [Composition(ram, 1), Composition(cpu,1)]


p4 = ProduitCompose("pc", "003",100, composition_p4)

print(cpu)
print(ram)

print(p4)
