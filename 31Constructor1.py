class Dog:
    name="Unknown"
    
    def set_name(self, name):
        self.name= name
        
    def bark(self, message):
        msg = f"Woof woof. My name is {self.name}. {message}"
        print(msg)
        print("Woof woof", message)
        
    def walk(self):
        print("Walking...")
        
dog1 =Dog("jksndkjwn") #meken call wenne function ekak. Eka penne na. Ex. like self parameter.
                       #python intepreter ekata internally athulath wela thiyenawa.
dog1.set_name("Scooby")
dog1.bark("Hi")

dog2= Dog()
#dog2.set_name("Droofy")
dog2.bark("Hello")

'''
TypeError: Dog() takes no arguments
'''