####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final - zoo
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 001
###  Description du fichier: Class reptile
####################################################################################
import json
from animaux import animal
from enclos import Enclos

class Reptile(animal.Animal):
    """
        classe Reptile
        """
    def __init__(self, p_enclos = Enclos(), p_poid = -1, p_nom = "" , p_espece = "", p_id = "", p_couleur_de_peau = "", p_temperature = ""):

        """
            Constructeur avec des paramètres par défaults pour la classe Reptile qui hérite d'animale
        """
        animal.Animal.__init__(self, p_enclos, p_poid, p_nom, p_espece, p_id, "Reptile")
        self.__couleur_de_peau = p_couleur_de_peau
        self.__temperature = p_temperature

    # Propriété pour temperature
    def _get_temperature(self) -> str:
        return self.__temperature

    # Doit être supérieur à 0
    def _set_temperature(self, p_temperature: float):

        if p_temperature > 0:
            self.__temperature = p_temperature

    Temperature = property(_get_temperature, _set_temperature)

    # Propriété pour couleur_de_peau
    def _get_couleur_de_peau(self) -> str:
        return self.__couleur_de_peau

    # Doit être supérieur à 0
    def _set_couleur_de_peau(self, p_couleur_de_peau: str):

        if p_couleur_de_peau.isalpha():
            self.__couleur_de_peau = p_couleur_de_peau

    Couleur_de_peau = property(_get_couleur_de_peau, _set_couleur_de_peau)
