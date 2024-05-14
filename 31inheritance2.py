class Animal:
    def __init__(self, breed):
        self.breed= breed
        
    def talk(self):
        print("Animal is talking")
        
    def move(self):
        print("Animal in moving")
        

class Dog(Animal):
    #constructor
    def __init__(self,name='Unknown'): 
        self.name= name
       
    def set_name(self, name):
        self.name= name
        
    def bark(self, message):
        msg = f"Woof woof. My name is {self.name}. {message}"
        print(msg)
             
    def walk(self):
        print("Walking...")
        
dog1 =Dog('Scooby') 
dog1.talk()

dog2= Dog()
dog2.bark("Hello")
print(dog1.breed)

'''
Animal is talking
Woof woof. My name is Unknown. Hello
Traceback (most recent call last):
  File "c:\Users\Anuradha\Desktop\Python\31inheritance2.py", line 32, in <module>
    print(dog1.breed)
          ^^^^^^^^^^
AttributeError: 'Dog' object has no attribute 'breed'

'''