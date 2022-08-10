class Complex:

    def __init__(self, nombre_reel1: int, nombre_imaginaire1: int, nombre_reel2:int, nombre_imaginaire2: int):
        self._nombre_reel1 = nombre_reel1
        self._nombre_imaginaire1 = nombre_imaginaire1
        self._nombre_reel2 = nombre_reel2
        self._nombre_imaginaire2 = nombre_imaginaire2




    def affichage_des_parties(self):
        total_nombre_reel = self._nombre_reel1 + self._nombre_reel2
        total_nombre_imaginaire = self._nombre_imaginaire1 + self._nombre_imaginaire2
        return f"la somme est {total_nombre_reel} + {total_nombre_imaginaire}i"
