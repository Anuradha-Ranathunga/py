class Dog:
    name=""
    breed= ""
    
    def set_name(self, name):
        self.name= name
        
    def bark(self, message):
        msg = f"Woof woof. My name is {self.name}. {message}"
        print(msg)
        print("Woof woof", message)
        
    def walk(self):
        print("Walking...")
        
dog1 =Dog()
dog1.set_name("Scooby")
dog1.bark("Hi")

dog2= Dog()
dog2.set_name("Droofy")
dog2.bark("Hello")

'''
Output =>
Woof woof. My name is Scooby. Hi
Woof woof Hi
Woof woof. My name is Droofy. Hello
Woof woof Hello

'''
