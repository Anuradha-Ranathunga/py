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

'''
Animal is talking
Woof woof. My name is Unknown. Hello
'''