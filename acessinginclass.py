# acess instance var in class method # not acessaible
# acess class var in class method # acess using cls
# acess static var in class method # acess using cls

class demo:
  x=100
  def name(self):
    self.name="trupti"

  @staticmethod
  def static_method():
    print("static method")

  @classmethod
  def class_demo(cls):
      print(cls.x)

      #acess static method
      cls.static_method()
demo.class_demo()      
     
