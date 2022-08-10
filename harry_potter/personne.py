class Personne():

    def __init__(self, nom_personne, prenom_personne, age_personne, vie_personne):
        self._nom_personne = nom_personne
        self._prenom_personne = prenom_personne
        self._age_personne = age_personne
        self._vie_personne = vie_personne

    @property
    def nom_personne(self):
        return self._nom_personne

    @nom_personne.setter
    def nom_personne(self, value):
        self._nom_personne = value


    @property
    def prenom_personne(self):
        return self._prenom_personne

    @prenom_personne.setter
    def prenom_personne(self, value):
        self._prenom_personne = value


    @property
    def age_personne(self):
        return self._age_personne

    @age_personne.setter
    def age_personne(self, value):
        self._age_personne = value


    @property
    def vie_personne(self):
        return self._vie_personne

    @vie_personne.setter
    def vie_personne(self, value):
        self._vie_personne = value


