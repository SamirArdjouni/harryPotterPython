from harry_potter.maison import Maison
from harry_potter.personne import Personne
from harry_potter.sort import Sort


class Sorcier(Personne):

    def __init__(self, nom_personne, prenom_personne, age_personne, point_fort_sorcier, point_faible_sorcier, nom_maison: Maison, liste_sorts):
        super().__init__(nom_personne, prenom_personne, age_personne, 100)
        self._point_fort_sorcier = point_fort_sorcier
        self._point_faible_sorcier = point_faible_sorcier
        self._maison = nom_maison
        self._liste_sorts = liste_sorts
        self._nom_personne = nom_personne
        self._prenom_personne = prenom_personne
        self._age_personne = age_personne

