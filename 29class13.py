class Dog:
    name=""
    breed=""
    
    def bark(self, message):
        print("Woof woof" ,  message)
        
    def walk(self):
        print("Walking...")
        
dog1 = Dog()

#Dog.walk() => There will be an error. 
#walk kiyanne object ekak haraha call karana function ekak. 

Dog.walk(dog1) #class ekak haraha function call karaddi explicitly object eka pass karanna wenawa. 