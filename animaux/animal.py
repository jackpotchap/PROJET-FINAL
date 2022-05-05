####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final - zoo
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 001
###  Description du fichier: Class Animal
####################################################################################

#importation
from enclos import Enclos
import json

class Animal:
    """
    classe Animal
    """
    def __init__(self, p_enclos = Enclos(), p_poid = 0, p_nom = "" , p_espece = "", p_id = ""):
        """
        Constructeur avec des paramètres par défaults pour la classe animale
        """
        self.__enclos = p_enclos
        self.__poid = p_poid
        self.__nom = p_nom
        self.__espece = p_espece
        self.__id = p_id

    #j'ai l'intention de faire un affichage dans une liste view donc pour me faciliter la tache je lais mis dans un dictionnaire
    def __str__(self):
        output = self.__dict__
        output["_Animal__enclos"] = self.Enclos.__str__()
        return str(output)

    #code tirée d'exemple vue en classe
    def serialiser(self, p_fichier):
        """
           Méthode pour sérialiser un object de la classe Animal.
           ::param p_fichier : Le nom du fichier de l'Animal.
        """
        with open(p_fichier , "w") as fichier:
            json.dump(self.__dict__, fichier)


    def deserialiser(self, p_fichier):
        """
           Méthode pour désérialiser un object de la classe Animal.
           ::param p_fichier : Le nom du fichier de l'Animal.
        """

        with open(p_fichier , "r") as fichier :
            self.__dict__ = json.load(fichier)


    #Propriété pour enclo
    def _get_enclo(self) -> Enclos:
        return self.__enclos
    #il n'y a pas de set car cette attribut est en lecture seulement
    Enclos = property(fget=_get_enclo)


    #Propriété pour poid
    def _get_poid(self) -> float:
        return self.__poid
    #Doit être supérieur à 0
    def _set_poid(self, p_poid: float):
        if p_poid > 0:
            self.__poid = p_poid

    Poid = property(_get_poid, _set_poid)


    #Propriété pour nom
    def _get_nom(self) -> str:
        return self.__nom
    #Doit être alphabétique
    def _set_nom(self, p_nom : str):
        if p_nom.isalpha():
            self.__nom = p_nom

    Nom = property(_get_nom,_set_nom)


    #Propriété pour espèce
    def _get_espece(self) -> str:
        return self.__espece
    #Doit être alphabétique
    def _set_espece(self, p_espece: str):
        if p_espece.isalpha():
            self.__espece = p_espece

    Espece = property(_get_espece, _set_espece)


    #Propriété pour id
    def _get_id(self) -> str:
        return self.__id
    #doit commencer par "A" et être suivit de 5 chiffre
    def _set_id(self, p_id: str):
        if len(p_id) == 6:
            if p_id[0] == "A":
                if p_id[1:].isnumeric():
                    self.__id = p_id

    Id = property(_get_id, _set_id)


