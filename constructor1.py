# to delcare a empty class need pass
class demo:
    pass


class demo1:
    pass
    #default constructor
    def __init__(self):
        print("object created")
    
    #parametrized constructor
    def __init__(self,age):
        self.name="abc"
        self.age=age
    
    # destructor
    def __del__(self):
        print("object destroyed")


obj=demo1(20)
print(obj.age)