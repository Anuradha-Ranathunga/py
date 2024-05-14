class Dog:
    name=""
    breed=""
    
    def bark(self, message):
        print("Woof woof", message)
        
dog1 = Dog()

dog1.bark("Hello")

dog2 = Dog()

dog2.bark("Hi")


'''
output=>
Woof woof Hello
Woof woof Hi

'''