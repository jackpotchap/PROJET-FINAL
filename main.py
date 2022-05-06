from animaux import animal
import enclos


def deserialiser_enclos(p_fichier):
    """
    Fonction qui permet de deserialier un enclo et l'integraliter des animaux qu'il contenait
    : p_fichier: le nom du fichier contenant l'enclo
    """
    enclo = enclos.Enclos()
    ls_animaux_t = enclo.deserialiser(p_fichier, [])
    for a in ls_animaux_t:
        a_t = animal.Animal(enclo, a["_Animal__poid_animal"], a["_Animal__nom_animal"], a["_Animal__espece_animal"], a["_Animal__id_animal"])
        ls_animaux.append(a_t)
    return enclo




