class Person:
    def __init__(self, name):
        self.name = name
        self.age = 25
        
    def sleep(self):
        print("Sleeping...", self.name)
        
Anuradha = Person("Anuradha")
Anuradha.sleep()
print("Name is ", Anuradha.name)
print("Age is ", Anuradha.age)

'''
Sleeping... Anuradha
Name is  Anuradha
Age is  25
'''