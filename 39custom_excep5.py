class Person:
    def __init__(self,name, age):
        super().__init__()
    
        self.name= name
        self.age = age
        
    @staticmethod
    def get_person(name,age):
        if not name:
            #create manually exception
            raise Exception("Invalid Name")
            print("Error")
        
        if age<0 or age>120:
            raise Exception("Invalid age")
            return
        
        return Person(name, age)

try:
    #create object        
    person =Person.get_person("" , -23)
    print(person)
except Exception as e:
    print("Error Found" , e)
    
print("Hello World")

'''
Error Found Invalid Name
Hello World
'''