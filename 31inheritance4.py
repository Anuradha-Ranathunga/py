class Animal:
    def __init__(self, breed):
        print("Hello from Animal")
        self.breed= breed
        
    def talk(self):
        print("Animal is talking")
        
    def move(self):
        print("Animal in moving")
        

class Dog(Animal):
    #Constructor
    #def __init__(self,name='Unknown'): 
    #   print("Dog is born!")
    #   self.name= name
       
    def set_name(self, name):
        self.name= name
        
    def bark(self, message):
        msg = f"Woof woof. My name is {self.name}. {message}"
        print(msg)
             
    def walk(self):
        print("Walking...")
        
dog1 =Dog('Scooby') 
dog1.talk()
#print(dog1.breed)

'''
Hello from Animal
Animal is talking
'''
#child class eke constructor ekak thibbe nattam automatically parent class eke constructor eka call karanawa.
#child class eke constructor eka call karana wita parent class eke constructor eka call karana eka nawaththanawa.
