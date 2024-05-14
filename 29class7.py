class Dog:
    name=""
    breed=""
    
    def bark(x): #python automatically object haraha parameter ekak pass karanawa object name ekenma. 
        print("Inside" , x)
        print("Woof woof")
        
dog1 = Dog()
print("Outside" , dog1)

dog1.bark()

'''

#output =>
Outside <__main__.Dog object at 0x000001D1C7C860C0>
Inside <__main__.Dog object at 0x000001D1C7C860C0>
Woof woof

'''
#Then x= dog1

#class ekaka function ekak define karaddi "self" parameter eka palaweni parameter eka wenna one.