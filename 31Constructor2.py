class Dog:
    name="Unknown"
    
    #constructor
    def __init__(self): #line 21 function eka externally call karanna
        print("Hello")
    #python walin constructor eka by default add karanawa. mehidi api explicitly add karala thiyenawa(override)
    #object eka hadana wita me fucntion eka automatically call wenawa.     
    
    def set_name(self, name):
        self.name= name
        
    def bark(self, message):
        msg = f"Woof woof. My name is {self.name}. {message}"
        print(msg)
        print("Woof woof", message)
        
    def walk(self):
        print("Walking...")
        
dog1 =Dog() #meken call wenne function ekak. Eka penne na. Ex. like self parameter
dog1.set_name("Scooby")
#dog1.bark("Hi")

dog2= Dog()
#dog2.set_name("Droofy")
dog2.bark("Hello")

'''
Hello
Hello
Woof woof. My name is Unknown. Hello
Woof woof Hello
'''
#object ekak hadaddi by default automatically call wena function eka => __init__