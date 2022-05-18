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
import copy

class Animal:
    """
    classe Animal
    """
    def __init__(self, p_enclos = Enclos(), p_poid = 0, p_nom = "" , p_espece = "", p_id = "", p_type = ""):
        """
        Constructeur avec des paramètres par défaults pour la classe animale
        """
        self.__enclos_animal = p_enclos

        self.__poid_animal = p_poid
        self.__nom_animal = p_nom
        self.__espece_animal = p_espece

        self.__id_animal = p_id
        self.__type = p_type


    #j'ai l'intention de faire un affichage dans une liste view donc pour me faciliter la tache je lais mis dans un dictionnaire
    #Une erreure survenait pusique il semblait changer la valeur dans l'objet et non pas juste du dictionaire
    #donc grace au code trouver sur https://www.programiz.com/python-programming/shallow-deep-copy#:~:text=In%20Python%2C%20we%20use%20%3D%20operator,reference%20of%20the%20original%20object.
    #je crée une copie ayant un pointeur différent a mon objet
    def __stre__(self):
        output = copy.copy(self.__dict__)

        output["_Animal__enclos_animal"] = self.Enclos_animal.Id_enclos

        return output

    #code tirée d'exemple vue en classe
    def serialiser(self, p_fichier):
        """
           Méthode pour sérialiser un object de la classe Animal.
           ::param p_fichier : Le nom du fichier de l'Animal.
        """


        with open(p_fichier , "w") as fichier:

            output = self.__dict__.copy()

            output["_Animal__enclos_animal"] = self.__enclos_animal.__dict__

            json.dump(output, fichier)


    def deserialiser(self, p_fichier, ls_enlclos, p_enclos_id = ""):
        """
           Méthode pour désérialiser un object de la classe Animal.
           ::param p_fichier : Le nom du fichier de l'Animal.
        """


        for enclos in ls_enlclos:
            #pour éviter les infinites loop l'enclos de l'animal contenue dans la list animal enclos represente seulement la variable et non
            #l'enclos si l'id de l'enclos est fournis ses qu'on souhait désirialiser toutes les animaux de cette enclos
            if p_enclos_id == "":
                with open(p_fichier, "r") as fichier:
                    self.__dict__ = json.load(fichier)
                if enclos.Id_enclos == self.__dict__["_Animal__enclos_animal"]['_Enclos__id_enclos']:
                    self.__dict__["_Animal__enclos_animal"] = enclos
            else:
                if enclos.Id_enclos ==p_enclos_id:
                    self.__dict__ = p_fichier
                    self.__dict__["_Animal__enclos_animal"] = enclos
    # Propriété pour type
    def _get_type(self) -> str:
        return self.__type

    Type = property(fget=_get_type)
    #Propriété pour enclo
    def _get_enclo_animal(self) -> Enclos:
        return self.__enclos_animal
    def _set_enclo_animal(self, p_enclo):
        self.__enclos_animal = p_enclo

    #il n'y a pas de set car cette attribut est en lecture seulement
    Enclos_animal = property(_get_enclo_animal, _set_enclo_animal)


    #Propriété pour poid
    def _get_poid_animal(self) -> float:
        return self.__poid_animal
    #Doit être supérieur à 0
    def _set_poid_animal(self, p_poid_animal: float):
        print(p_poid_animal > 0)
        if p_poid_animal > 0:
            self.__poid_animal = p_poid_animal

    Poid_animal = property(_get_poid_animal, _set_poid_animal)


    #Propriété pour nom
    def _get_nom_animal(self) -> str:
        return self.__nom_animal
    #Doit être alphabétique
    def _set_nom_animal(self, p_nom_animal : str):
        if p_nom_animal.isalpha():
            self.__nom_animal= p_nom_animal

    Nom_animal = property(_get_nom_animal,_set_nom_animal)


    #Propriété pour espèce
    def _get_espece_animal(self) -> str:
        return self.__espece_animal
    #Doit être alphabétique
    def _set_espece_animal(self, p_espece: str):

        #j'utilise le replace pour enlever les espace puisque il ne sont pas alphabétique
        #mais que le nom d'une espece peut contenir des espace
        if p_espece.replace(" ","").isalpha():
            self.__espece_animal = p_espece

    Espece = property(_get_espece_animal, _set_espece_animal)


    #Propriété pour id
    def _get_id_animal(self) -> str:
        return self.__id_animal
    #doit commencer par "A" et être suivit de 5 chiffre
    def _set_id_animal(self, p_id_animal: str):
        if len(p_id_animal) == 6:
            if p_id_animal[0] == "A":
                if p_id_animal[1:].isnumeric():
                    self.__id_animal = p_id_animal

    Id_animal = property(_get_id_animal, _set_id_animal)


