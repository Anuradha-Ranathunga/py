class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 25
        
    def get_age(self):
        return self.__age
        
    def sleep(self):
        print("Sleeping...", self.name)
        
Anuradha = Person("Anuradha")
Anuradha.sleep()
#Anuradha.__age= 50
print("Name is ", Anuradha.name)
print("Age is ", Anuradha.get_age()) #private variable eka eliyata return karanna

'''
Sleeping... Anuradha
Name is  Anuradha
Age is  25
'''