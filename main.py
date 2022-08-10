from turtle import distance

from exoPoo1 import Rectangle
from exoPoo2 import Somme
# from exoPoo3 import Student
from exoPoo4 import Complex
from exoPoo5 import Point
# from module.person import Person
# from module import Student, Person
# from harry_potter import *
from harry_potter import Eleve, Sorcier, Sort
from harry_potter import eleve
from module import *

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# def main():
#     student = Student()
#     print(student.calc_moy())
# if __name__ == '__main__':
#     main()

# ============ EXO1 =========================

# rectangle_1 = Rectangle(12, 5)
# print(rectangle_1)
# print(rectangle_1.surface())
#
# rectangle_2 = Rectangle(2,4)
# rectangle_2.surface()
# print(rectangle_2)
#
# # ============ EXO2 =========================
#
# n1 = int(input("veuillez saisir un premier nombre "))
# n2 = int(input("veuillez saisir un second nombre "))
# somme = Somme(n1, n2)
# sum1 = somme.sum()
# # print("je suis la somme un", sum1)


# ============ EXO3 =========================

# nom = input("veuillez saisir votre nom ")
# note1 = int(input("veuillez saisir un premier nombre "))
# note2 = int(input("veuillez saisir un premier nombre "))
# eleve1 = Student(nom, note1, note2)
# # print(eleve1.calc_moy())
# print(eleve1)

# ============ EXO4 =========================

# print("PREMIER NOMBRE")
# nombre_reel1 = int(input("Entrer la partie réelle: "))
# nombre_imaginaire1 = int(input("Entrer la partie imaginaire: "))
#
# print("DEUXIEME NOMBRE")
# nombre_reel2 = int(input("Entrer la partie réelle: "))
# nombre_imaginaire2 = int(input("Entrer la partie imaginaire: "))
#
# affichage = Complex(nombre_reel1, nombre_imaginaire1, nombre_reel2, nombre_imaginaire2)
# print(affichage)
# print(affichage.affichage_des_parties())

# ============ EXO5 =========================

# print("P1")
# nombre_reel1 = int(input("Entrer le premier nombre X: "))
# nombre_imaginaire1 = int(input("Entrer le premier nombre Y: "))
#
# print("P2")
# nombre_reel2 = int(input("Entrer le second nombre X: "))
# nombre_imaginaire2 = int(input("Entrer le second nombre Y: "))
#
# distance = Point(nombre_reel1, nombre_imaginaire1, nombre_reel2, nombre_imaginaire2)
# print(distance)
# print(distance.distance())


# ============ EXO6 =========================

    # def main():
    #     print("Hello World!")
    #     personne_1 = Person(25)
    #     personne_1.say_hello()
from module.student import Student
from module.teacher import Teacher


def main():
    # student = Student()
    # personne_1 = Person(25)
    # print("je suis la personne 1 " + personne_1.say_hello())
    #
    # student_1 = Student(15)
    # print("je suis l'etudiant 1 " + student_1.say_hello())
    # print(student_1.go_to_lasses())
    # print(student_1.display_age())
    #
    # teacher_1 = Teacher(40, "coucou")
    # print("je suis le professeur 1 " + teacher_1.say_hello())
    # print(teacher_1.explain())

    #           EXO HARRY POTTERRRRRRRRRRRRRRRRRRRRRRRR

    magie = Sort("toto", "vert", "malédiction", 12, 0)
    liste_sorts = []
    liste_sorts.append(magie)
    sorcier_1 = Sorcier("nom samir", "prenom sam", 30, "force", "endurance", "maison ASTON", liste_sorts)
    print(sorcier_1)
    # eleve_1 = Eleve("épée", "magie", "i don't know")
    # print(eleve_1)


if __name__ == '__main__':
    main()