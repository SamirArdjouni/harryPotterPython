class Maison():

    def __init__(self, nom_maison, couleur_principale_maison):
        self._nom_maison = nom_maison
        self.couleur_principale_maison = couleur_principale_maison


    @property
    def nom_maison(self):
        return self._nom_maison

    @nom_maison.setter
    def nom_maison(self, value):
        self._nom_maison = value


    @property
    def couleur_principale_maison(self):
        return self._couleur_principale_maison

    @couleur_principale_maison.setter
    def couleur_principale_maison(self, value):
        self._couleur_principale_maison = value