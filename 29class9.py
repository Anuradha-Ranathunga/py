class Dog:
    name = ""
    breed = ""
    
    def bark(self,message):
        print("Inside", self)
        print("Woof woof", message)
         
dog1= Dog()
print("Outside", dog1)
dog1.bark("Hello")

'''
output =>
Outside <__main__.Dog object at 0x000002562C526210>
Inside <__main__.Dog object at 0x000002562C526210>
Woof woof Hello

'''