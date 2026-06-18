globalvar = "hey"

class Demo1:

    def __init__(self):
        print("Object created")

    def acess_var(self):
        print(globalvar)

        self.localvar = 90    # Instance variable
        print(self.localvar)

    def acess_local(self):
        print(self.localvar)


obj = Demo1()

obj.acess_var()      # Creates self.localvar
obj.acess_local()    # Accesses self.localvar

print(globalvar)