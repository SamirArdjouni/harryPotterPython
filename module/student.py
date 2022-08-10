from module.person import Person

class Student(Person):

    def __init__(self, age):
        super().__init__(age)

    def go_to_lasses(self):
        return "I’m going to class. "

    def display_age(self):
        return f"My age is {super().display_age()}"

        # return f"My age is: {self.age} years old : {super().display_age()}"


        # + plubic
        # - private
