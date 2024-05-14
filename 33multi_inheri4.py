class Animal:
    def __init__(self, breed="Unknown"):
        print("Hello from Animal")
        self.breed= breed
        
    def talk(self):
        print("Animal is talking")
        
    def move(self):
        print("Animal in moving")
        
    def feed(self):
        print("Animal is feeding")
        
class Mammal:
    def __init__(self):
        print("I'm a Mammal")
        
    def feed(self):
        print("Drinking Milk")
        

class Dog(Mammal, Animal):
    #Constructor
    def __init__(self,name='Unknown'): 
        #breed initialize kireema sadaha
        super(Dog, self). __init__() #parent class eke init function eka call karala ita adala parameter eka pass karanawa. 
                                     #breed argument eka thibbe nattam "Dog" parameter pass karanna awashya na. 
        print("Dog is born!")
        self.name= name
       
    def set_name(self, name):
        self.name= name
        
#overriding        
    def talk(self):
        
        print("Dog is talking.")
        super(Dog, self).talk() #super dana thana anuwa issella print wenne child function ekada parent function ekada yanna decide wenawa. 
    
    def feed(self):
        print("Dog is feeding")
        super(Dog,self).feed()
        
    def bark(self, message):
        msg = f"Woof woof. My name is {self.name}. {message}"
        print(msg)
             
    def walk(self):
        print("Walking...")
        
dog1 =Dog('Scooby') 
dog1.feed()

'''
I'm a Mammal
Dog is born!
Dog is feeding
Drinking Milk
'''
#inherit karana order eka final output ekata balapanawa. 