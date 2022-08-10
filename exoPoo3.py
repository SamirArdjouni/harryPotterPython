class Student:

    def __init__(self, nom: str, note1: int, note2: int):
        self._nom = nom
        self._note1 = note1
        self._note2 = note2

    @property
    def nom(self):
        return self._nom

    @property
    def note1(self):
        return self._note1

    @property
    def note2(self):
        return self._note2

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @note1.setter
    def note1(self, note1):
        if (type(note1) is not int):
            raise TypeError("merci de saisir un nombre svp")
        self._note1 = note1

    @note2.setter
    def note1(self, note2):
        if (type(note2) is not int):
            raise TypeError("merci de saisir un nombre svp")
        self._note2 = note2

    def calc_moy(self):
        return (self._note1 + self._note2) / 2


    def __str__(self):
        return f"{self._nom} à une moyenne de  {str(self.calc_moy())}"