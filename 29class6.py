class Dog:
    name=""
    breed=""
    
    def bark(x): #python automatically object haraha parameter ekak pass karanawa object name ekenma. 
        print(type(x), x)
        print("Woof woof")
        
dog1 = Dog()

dog1.bark()

#output => <class '__main__.Dog'> <__main__.Dog object at 0x0000012BC28C5FD0> Woof woof