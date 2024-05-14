#private => __age , __name
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 25
        
    def sleep(self):
        print("Sleeping...", self.name)
        
Anuradha = Person("Anuradha")
Anuradha.sleep()
#Anuradha.age= 50
print("Name is ", Anuradha.name)
print("Age is ", Anuradha.__age)

'''
AttributeError: 'Person' object has no attribute '__age'
'''