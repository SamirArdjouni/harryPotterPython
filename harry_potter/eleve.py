from harry_potter import Sorcier, Maison


class Eleve(Sorcier):

    def __init__(self, point_fort_sorcier, point_faible_sorcier, nom_maison:Maison):
        super().__init__(self, point_fort_sorcier, point_faible_sorcier, nom_maison)
        self.vie_personne = 100
        self._point_fort_sorcier = point_fort_sorcier
        self._point_faible_sorcier = point_faible_sorcier
        self._nom_maison = nom_maison

        # super(Eleve, self).__init__()

        # self.vie_personne = 100
    #super().__init__(self, point_fort_sorcier, point_faible_sorcier, nom_maison: Maison)
    # , point_fort_sorcier, point_faible_sorcier, nom_maison : Maison, nom_sort : Sort