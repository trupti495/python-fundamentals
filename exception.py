# using simple try and except block
"""
try:
    # risky code
except:
    # handles exception
else:
    # runs if no exception occurs
finally:
    # always runs
try:
    print(10/2)
except ZeroDivisionError as a:
    print(a) 

    """
# using simple try and multiple catch block
try:
    a=int(input("enter first number :"))
    b=int(input("enter second number :")) 
    print(a/b)
except ZeroDivisionError as e:
    print("divide by zero error")
except ValueError as v:
    print(" value error") 

# using else block
# else block is executed when error is not genrate
try:
    a=int(input("enter first number :"))
    b=int(input("enter second number :")) 
    print(a/b)
except ZeroDivisionError as e:
    print("divide by zero error")
except ValueError as v:
    print(" value error") 
else:
    print("program executed successfully")

#finally block is run every times 
print("finally block")
try:
    a=int(input("enter first number :"))
    b=int(input("enter second number :")) 
    print(a/b)
except ZeroDivisionError as e:
    print("divide by zero error")
except ValueError as v:
    print(" value error") 
finally:
    print("i am always executed")    
    
