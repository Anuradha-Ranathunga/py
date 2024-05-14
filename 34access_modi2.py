class Person:
    def __init__(self, name):
        self.name = name
        self.age = 25
        
    def sleep(self):
        print("Sleeping...", self.name)
        
Anuradha = Person("Anuradha")
Anuradha.sleep()
Anuradha.age= 50
print("Name is ", Anuradha.name)
print("Age is ", Anuradha.age)

'''
Sleeping... Anuradha
Name is  Anuradha
Age is  50
'''
#Age pitatha idan access kirima nawattanna one. e sadaha Access modifiers yoda ganiyi