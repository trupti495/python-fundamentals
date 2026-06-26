# acess instace var in instance method
# acess class var in instance method
# acess static var in instance var

class Student:
    college = "ABC College"     # Class variable

    @staticmethod
    def greet():
        print("Hello")          # Static method

    def show(self):
        self.name = "Trupti"    # Instance variable

        # Access instance variable
        print(self.name)

        # Access class variable
        print(Student.college)   # or self.college

        # Access static method
        Student.greet()          # or self.greet()

s = Student()
s.show()