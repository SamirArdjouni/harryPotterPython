from module.person import Person


class Teacher(Person):

    def __init__(self, age, subject):
        super().__init__(age)
        self.__subject__ = subject

    def explain(self):
        return "Explanation begins"