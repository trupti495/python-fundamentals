# exception handling in python
# handle multiple exception 
def add():
  try:
   a=int(input("enter first number :"))
   b=int(input("enter second number ;"))
   result=a+b
   print("addition=",result)
  
  except ValueError as e:
    print(e)
  except Exception as e:
    print(e)
  else:
    print("program executed successfully")  

add()