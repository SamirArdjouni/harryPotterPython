class Person:

    def __init__(self, age):
        self.__age = age

    def display_age(self):
        return f"{self.__age}years old"

    @property
    def age(self):
        return self.__age

    def say_hello(self):
        return "Hello"
