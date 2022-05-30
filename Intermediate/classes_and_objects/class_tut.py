

class Student:

    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        pass

    def is_distinction(self):
        if self.gpa >= 4:
            print("True")