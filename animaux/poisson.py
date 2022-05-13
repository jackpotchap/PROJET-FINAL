####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final - zoo
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 001
###  Description du fichier: Class poisson
####################################################################################
import json
from animaux import animal
from enclos import Enclos

class Poisson(animal.Animal):
    """
        classe poisson
        """
    def __init__(self, p_enclos = Enclos(), p_poid = -1, p_nom = "" , p_espece = "", p_id = "", p_longueur_des_nageoire = -1, p_profondeur_moyenne = -1):
        """
            Constructeur avec des paramètres par défaults pour la classe poisson qui hérite d'animale
        """
        animal.Animal.__init__(self, p_enclos, p_poid, p_nom, p_espece, p_id)
        self.__longueur_des_nageoire = p_longueur_des_nageoire
        self.__profondeur_moyenne = p_profondeur_moyenne

    # Propriété pour longueur_des_nageoire
    def _get_longueur_des_nageoire(self) -> float:
        return self.__longueur_des_nageoire

    # Doit être supérieur à 0
    def _set_longueur_des_nageoire(self, p_longueur_des_nageoire: float):
        if p_longueur_des_nageoire > 0:
            self.__longueur_des_nageoire = p_longueur_des_nageoire

    Longueur_des_nageoire = property(_get_longueur_des_nageoire, _set_longueur_des_nageoire)

    # Propriété pour profondeur_moyenne
    def _get_profondeur_moyenne(self) -> float:
        return self.__profondeur_moyenne

    # Doit être supérieur à 0
    def _set_profondeur_moyenne(self, p_profondeur_moyenne: float):
        if p_profondeur_moyenne > 0:
            self.__profondeur_moyenne = p_profondeur_moyenne

    Profondeur_moyenne = property(_get_profondeur_moyenne, _set_profondeur_moyenne)

