from animaux import reptile, oiseau, poisson
import enclos

ls_animaux = [reptile.Reptile(p_id="A12345")]
ls_enclos = [enclos.Enclos("Plaine", [], "2006-06-06", "E12345")]
ls_type_enclos = ["Plaines","Marais","Jungle","Taïga","Toundra enneigée"]
dict_classe_animaux = {"Reptile" : reptile.Reptile , "Oiseau" : oiseau.Oiseau, "Poisson": poisson.Poisson}