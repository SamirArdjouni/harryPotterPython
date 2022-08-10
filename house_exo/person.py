from house_exo.house import House


class Person(House):
    def __init__(self, surface, nom):
        super().__init__(self, surface)
        self.__nom = nom

    def display_house(self):
