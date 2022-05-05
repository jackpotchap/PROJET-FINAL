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
        self.__enclos_animal = p_enclos
        self.__poid_animal = p_poid
        self.__nom_animal = p_nom
        self.__espece_animal = p_espece
        self.__id_animal = p_id

    #j'ai l'intention de faire un affichage dans une liste view donc pour me faciliter la tache je lais mis dans un dictionnaire
    def __stre__(self):
        output = self.__dict__
        output["_Animal__enclos_animal"] = self.Enclos_animal.__str__()
        return str(output)

    #code tirée d'exemple vue en classe
    def serialiser(self, p_fichier):
        """
           Méthode pour sérialiser un object de la classe Animal.
           ::param p_fichier : Le nom du fichier de l'Animal.
        """
        with open(p_fichier , "w") as fichier:
            output = self.__dict__
            output["_Animal__enclos_animal"] = self.Enclos_animal.__str__()
            json.dump(output, fichier)


    def deserialiser(self, p_fichier):
        """
           Méthode pour désérialiser un object de la classe Animal.
           ::param p_fichier : Le nom du fichier de l'Animal.
        """

        with open(p_fichier , "r") as fichier :
            self.__dict__ = json.load(fichier)


    #Propriété pour enclo
    def _get_enclo_animal(self) -> Enclos:
        return self.__enclos_animal
    #il n'y a pas de set car cette attribut est en lecture seulement
    Enclos_animal = property(fget=_get_enclo_animal)


    #Propriété pour poid
    def _get_poid_animal(self) -> float:
        return self.__poid
    #Doit être supérieur à 0
    def _set_poid_animal(self, p_poid_animal: float):
        if p_poid_animal > 0:
            self.__poid = p_poid_animal

    Poid_animal = property(_get_poid_animal, _set_poid_animal)


    #Propriété pour nom
    def _get_nom_animal(self) -> str:
        return self.__nom
    #Doit être alphabétique
    def _set_nom_animal(self, p_nom_animal : str):
        if p_nom_animal.isalpha():
            self.__nom = p_nom_animal

    Nom_animal = property(_get_nom_animal,_set_nom_animal)


    #Propriété pour espèce
    def _get_espece(self) -> str:
        return self.__espece
    #Doit être alphabétique
    def _set_espece(self, p_espece: str):
        if p_espece.isalpha():
            self.__espece = p_espece

    Espece = property(_get_espece, _set_espece)


    #Propriété pour id
    def _get_id_animal(self) -> str:
        return self.__id_animal
    #doit commencer par "A" et être suivit de 5 chiffre
    def _set_id_animal(self, p_id_animal: str):
        if len(p_id_animal) == 6:
            if p_id_animal[0] == "A":
                if p_id_animal[1:].isnumeric():
                    self.__id = p_id_animal

    Id_animal = property(_get_id_animal, _set_id_animal)


