####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final - zoo
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 001
###  Description du fichier: Class Enclos
####################################################################################
import json


class Enclos:
    """
        classe enclos
        """

    def __init__(self, p_ecosysteme="plaine", p_ls_animaux = [], p_dernier_netoyage="", p_id=""):
        """
        Constructeur avec des paramètres par défaults pour la classe enclos
        """
        self.Ecosysteme_enclos = p_ecosysteme
        self.Ls_animaux_enclos = p_ls_animaux
        self.Dernier_netoyage_enclos = p_dernier_netoyage
        self.__id_enclos = p_id

    # j'ai l'intention de faire un affichage dans une liste view donc pour me faciliter la tache je lais mis dans un dictionnaire
    def __str__(self):
        output = self.__dict__

        ls_animale_t = []
        for a in self.Ls_animaux_enclos:
            dict_t = a.__dict__
            dict_t["_Animal__enclos_animal"] = a.ID
            ls_animale_t.append(dict_t)

        return str(output)

        # code tirée d'exemple vue en classe
    def serialiser(self, p_fichier):
        """
           Méthode pour sérialiser un object de la classe enclos.
           ::param p_fichier : Le nom du fichier de l'enclos.
        """
        output = self.__dict__
        ls_animale_t = []
        for a in self.Ls_animaux_enclos:
            dict_t = a.__dict__
            dict_t["_Animal__enclos_animal"] = self.Id_enclos
            ls_animale_t.append(dict_t)

        output["Ls_animaux_enclos"] = ls_animale_t

        with open(p_fichier, "w") as fichier:

            json.dump(output, fichier)


    def deserialiser(self, p_fichier,ls_animaux):
        """
           Méthode pour désérialiser un object de la classe enclos.
           ::param p_fichier : Le nom du fichier de l'enclos.
        """
        trouver = False
        with open(p_fichier, "r") as fichier:
            self.__dict__ = json.load(fichier)
            for animal in ls_animaux:
                if animal.Id_animal == self.__dict__["_Animal__enclos_animal"]:
                    self.__dict__["_Animal__enclos_animal"] = self
                    trouver = True

            if not trouver:
                return self.Ls_animaux_enclos

    # Propriété pour id
    def _get_id_enclos(self) -> str:
        return self.__id_enclos

    # doit commencer par "E" et être suivit de 5 chiffre
    def _set_id_enclos(self, p_id_enclos: str):
        if len(p_id_enclos) == 6:
            if p_id_enclos[0] == "E":
                if p_id_enclos[1:].isnumeric():
                    self.__id_enclos = p_id_enclos

    Id_enclos = property(_get_id_enclos, _set_id_enclos)




