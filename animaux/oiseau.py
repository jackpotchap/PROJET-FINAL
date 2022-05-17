####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final - zoo
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 001
###  Description du fichier: Class oiseau
####################################################################################
import json
from animaux import animal
from enclos import Enclos

class Oiseau(animal.Animal):
    """
        classe oiseau
        """
    def __init__(self, p_enclos = Enclos(), p_poid = -1, p_nom = "" , p_espece = "", p_id = "", p_longeur_des_ailes = -1, p_longeur_bec = -1):
        """
            Constructeur avec des paramètres par défaults pour la classe oiseau qui hérite d'animale
        """

        animal.Animal.__init__(self, p_enclos, p_poid, p_nom, p_espece, p_id, "Oiseau")

        self.__longeur_des_ailes = p_longeur_des_ailes
        self.__longeur_bec = p_longeur_bec

    # Propriété pour longeur_des_ailes
    def _get_longeur_des_ailes(self) -> float:
        return self.__longeur_des_ailes

    # Doit être supérieur à 0
    def _set_longeur_des_ailes(self, p_longeur_des_ailes: float):
        if p_longeur_des_ailes > 0:
            self.__longeur_des_ailes = p_longeur_des_ailes

    Longeur_des_ailes = property(_get_longeur_des_ailes, _set_longeur_des_ailes)

    # Propriété pour longeur_bec
    def _get_longeur_bec(self) -> float:
        return self.__longeur_bec

    # Doit être supérieur à 0
    def _set_longeur_bec(self, p_longeur_bec: float):
        if p_longeur_bec > 0:
            self.__longeur_bec = p_longeur_bec

    Longeur_bec = property(_get_longeur_bec, _set_longeur_bec)


