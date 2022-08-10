import self as self


class Rectangle:
    """
    classe qui calcul la surface d'un rectangle

    attributs:
        a(int): longeur du rectangle
        b(int): largeur du rectangle
    """

    def __init__(self, a:int, b:int):
        self._longeur = a
        self._largeur = b

    @property
    def longeur(self):
        return self._longeur

    @property
    def largeur(self):
        return self._largeur

    @longeur.setter
    def longeur(self, longeur):
        if (type(longeur) is not int):
            raise TypeError("merci de saisir un nombre svp")
        self._longeur = longeur

    @largeur.setter
    def largeur(self, largeur):
        if (type (largeur) is not int):
            raise TypeError("merci de saisir un nombre svp")
        self._largeur = largeur

    def __str__(self):
        return f"{self._longeur}, {self._largeur}"

    def surface(self):
        return self._longeur*self._largeur

    def sum(self, nombre_1, nombre_2):
        return f"La surface de {self._longeur} et de {self._largeur} "