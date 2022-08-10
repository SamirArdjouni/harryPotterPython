class Somme:
    """
        classe qui calcul la surface d'un rectangle

        attributs:
            n1(int): longeur du rectangle
            n2(int): largeur du rectangle
    """

    def __init__(self, n1:int, n2:int):
        self._nombre1 = n1
        self._nombre2 = n2
        # sum(self.nombre1, self.nombre2)

    @property
    def nombre1(self):
        return self._nombre1

    @property
    def nombre2(self):
        return self._nombre2


    @nombre1.setter
    def nombre1(self, nombre1):
        if (type(nombre1) is not int):
            raise TypeError("merci de saisir un nombre svp")
        self._nombre1 = nombre1

    @nombre2.setter
    def nombre2(self, nombre2):
        if (type(nombre2) is not int):
            raise TypeError("merci de saisir un nombre svp")
        self._nombre2 = nombre2



    def sum(self):
        return f"La somme de {self._nombre1} et de {self._nombre2} est: {self._nombre1 + self._nombre2}"


    def __str__(self):
        return f"La somme de {self.nombre1} et de {self.nombre2} est: {sum(self.nombre2 +self.nombre1)}"