# instance method
# An instance method works with a specific object of a
#  class. It takes self as its first parameter.

class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

# not able to call using class
s1 = Student("Trupti")
s1.show()