class Sort():

    def __init__(self, nom_sort, couleur_sort, categorie_sort, degat_sort, vie_sort):
        self._nom_sort = nom_sort
        self._couleur_sort = couleur_sort
        self._categorie_sort = categorie_sort
        self._degat_sort = degat_sort
        self._vie_sort = vie_sort


    @property
    def nom_sort(self):
        return self._nom_sort

    @nom_sort.setter
    def nom_sort(self, value):
        self._nom_sort = value


    @property
    def couleur_sort(self):
        return self._couleur_sort

    @couleur_sort.setter
    def couleur_sort(self, value):
        self._couleur_sort = value


    @property
    def categorie_sort(self):
        return self._categorie_sort

    @categorie_sort.setter
    def categorie_sort(self, value):
        self._categorie_sort = value



    @property
    def degat_sort(self):
        return self._degat_sort

    @degat_sort.setter
    def degat_sort(self, value):
        self._degat_sort = value



    @property
    def vie_sort(self):
        return self._vie_sort

    @vie_sort.setter
    def vie_sort(self, value):
        self._vie_sort = value

