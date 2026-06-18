# instance varibale and class varibale
# An instance variable is a variable
# that belongs to an object (instance) of a class. It is created using self.

class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age        # instance variable
    
    def display(self):
        print("name :",self.name) # to acess the instance var in diffrent method we need self
        print("age :",self.age)

s1 = Student("Trupti", 20)

# to acess the instance var outside the class we need a objectname.variablename
print(s1.name)
s1.display()

# class variable
#A class variable is 
#a variable declared inside a class but outside all methods. It is shared by all objects of that class.

class Student:

    college = "ABC College"   # Class Variable

    def show(self):
        print("College:", self.college)


# Access using class name
print(Student.college)

# Access using object
s1 = Student()
print(s1.college)

# Access inside method
s1.show()