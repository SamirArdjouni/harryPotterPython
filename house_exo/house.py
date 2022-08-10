class House():

    def __init__(self, surface, door):
        self.__surface = surface


    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, surface):
        self.__surface = surface

    def display_house (self):
        return f"« Je suis une maison, ma surface est de {self.__surface} m2"

    def get_door(self):
        return f"je suis une porte de couleur {self.color}"

    # return f"My age is: {self.age} years old : {super().display_age()}"