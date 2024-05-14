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
    def __init__(self,name='Unknown'): 
        #breed initialize kireema sadaha
        super(Dog, self). __init__("Dog") #parent class eke init function eka call karala ita adala parameter eka pass karanawa. 
                                          #breed argument eka thibbe nattam "Dog" parameter pass karanna awashya na. 
        print("Dog is born!")
        self.name= name
       
    def set_name(self, name):
        self.name= name
        
    def talk(self):
        print("Dog is talking.")
        
    def bark(self, message):
        msg = f"Woof woof. My name is {self.name}. {message}"
        print(msg)
             
    def walk(self):
        print("Walking...")
        
dog1 =Dog('Scooby') 
dog1.talk()
print(dog1.breed)

'''
Hello from Animal
Dog is born!
Dog is talking.
Dog
'''

#child class eke talk function eka call unata passe parent class eke talk call karanne na. 