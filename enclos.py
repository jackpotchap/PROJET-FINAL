####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final - zoo
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 001
###  Description du fichier: Class Enclos
####################################################################################
import json
from animaux import animal

class Enclos:
    """
        classe enclos
        """

    def __init__(self, p_ecosysteme="plaine", p_ls_animaux = [], p_dernier_netoyage="", p_id=""):
        """
        Constructeur avec des paramètres par défaults pour la classe enclos
        """
        self.Ecosysteme = p_ecosysteme
        self.Ls_animaux = p_ls_animaux
        self.Dernier_netoyage = p_dernier_netoyage
        self.__id = p_id

    # j'ai l'intention de faire un affichage dans une liste view donc pour me faciliter la tache je lais mis dans un dictionnaire
    def __str__(self):
        output = self.__dict__
        return str(output)


    # Propriété pour id
    def _get_id(self) -> str:
        return self.__id

    # doit commencer par "E" et être suivit de 5 chiffre
    def _set_id(self, p_id: str):
        if len(p_id) == 6:
            if p_id[0] == "E":
                if p_id[1:].isnumeric():
                    self.__id = p_id

    Id = property(_get_id, _set_id)





