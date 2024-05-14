class Animal:
    def __init__(self, breed):
        print("Hello from Animal")
        self.breed= breed
        
    def talk(self):
        print("Animal is talking")
        
    def move(self):
        print("Animal in moving")
        

class Dog(Animal):
    #constructor
    def __init__(self,name='Unknown'): 
        print("Dog is born!")
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

#print(dog1.breed)

'''
Dog is born!
Animal is talking
'''
#Dog function eka hadeddi Dog class eke constructor eka call unata animal constructor eka call wenne na. 