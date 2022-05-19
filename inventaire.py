####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: le fichier qui contient les information gloabal de tous le zoo
###################################################################################

from animaux import reptile, oiseau, poisson
import enclos

ls_enclos = [enclos.Enclos("Plaine", [], "2006-06-06", "E12345"), enclos.Enclos("Marais", [], "2020-01-11", "E12367")]
#list qui seras utile lorsque la list_view seras filtré

ls_enclos_filtrer = []

ls_animaux = [oiseau.Oiseau(p_id="A12945", p_nom="pascale",p_poid=19, p_espece="Strigops habroptila", p_longeur_bec=20, p_enclos=ls_enclos[0], p_longeur_des_ailes=89)]

#list qui seras utile lorsque la list_view seras filtré

ls_animaux_filtrer = []
ls_type_enclos = ["Plaine","Marais","Jungle","Taïga","Toundra en neigée"]

ls_enclos[0].Ls_animaux_enclos.append(ls_animaux[0])


dict_classe_animaux = {"Reptile" : reptile.Reptile , "Oiseau" : oiseau.Oiseau, "Poisson": poisson.Poisson}


#un dict qui vas me permetre de savoir de quelle type un animal est
dict_translate_object_to_dict = {type(reptile.Reptile()): "Reptile",
                                 type(oiseau.Oiseau()): "Oiseau",
                                 type(poisson.Poisson()): "Poisson",}