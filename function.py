# functions are of two type 1 pre 2 userdefined
# after that 4 types

# function without arg without return value
# function without arg return value
# function with arg without return value
# function with arg with return value

# function without arg without return value
def greet():
    print("hello")
greet()    

# function with arg without return value
def wish(name):
    print("hello",name)

wish("trupti")

# function with arg with return value
# during calling of this function we have two way
# 1 way directly call inside print 
# 2 way to assign the result in particular variable

print("function with argument with return value")
def name(name):
    return f"heyy {name}"

print(name("trupti"))

# function without arg with return value

def name_c():
    return " i am trupti"

str=name_c()
print(str)