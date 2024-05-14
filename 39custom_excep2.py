class Person:
    def __init__(self,name, age):
        super().__init__()
    
        self.name= name
        self.age = age
        
    @staticmethod
    def get_person(name,age):
        if not name:
            print("Invalid name")
            return
        
        if age<0 or age>120:
            print("Invalid age")
            return
        
        return Person(name, age)

#create object        
person =Person.get_person("Anu" , -23)
print(person)

'''
Invalid age
None
'''
