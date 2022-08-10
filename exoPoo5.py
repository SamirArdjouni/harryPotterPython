import math


class Point:

    def __init__(self, nombre_reel1, nombre_imaginaire1, nombre_reel2, nombre_imaginaire2 ):
        self._nombre_reel1 = nombre_reel1
        self._nombre_imaginaire1 = nombre_imaginaire1
        self._nombre_reel2 = nombre_reel2
        self._nombre_imaginaire2 = nombre_imaginaire2


    def distance(self):
        p1 = (self._nombre_imaginaire1 - self._nombre_reel1) **2
        p2 = (self._nombre_imaginaire2 - self._nombre_reel2) **2
        distance = math.sqrt(p1 - p2)
        return f"La distance entre P1 et P2 est: {round(distance,2)}"


