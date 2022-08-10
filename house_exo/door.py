class Door():

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.surface(self, color):
        self.__color = color

    def display_door(self):
        return f"Je suis une porte, ma couleur est {self.__color}"
