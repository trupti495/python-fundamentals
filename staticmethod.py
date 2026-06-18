# static method
#A static method belongs to the class but does not use
#  self (object) or cls (class).
#  It is defined using the @staticmethod decorator.

class Student:

    @staticmethod
    def greet():
        print("Welcome Students")


    def display(self, name):
        self.name = name    

# to acess static method need object or class to acess
s1= Student()
s1.greet()
Student.greet()