class InvalidNameException(Exception):
    def __init__(self,error):
        super(InvalidNameException, self).__init__(error)
        self.error_code = 10
        
class InvalidAgeException(Exception):
    def __init__(self,error):
        super(InvalidAgeException, self).__init__(error)
        self.error_code = 5

class Person:
    def __init__(self,name, age):
        super().__init__()
    
        self.name= name
        self.age = age
        
    @staticmethod
    def get_person(name,age):
        if not name:
            #create manually exception
            raise InvalidNameException("Invalid Name")
            print("Error")
        
        if age<0 or age>120:
            raise InvalidAgeException("Invalid age")
            return
        
        return Person(name, age)

try:
    #create object        
    person =Person.get_person("" , -23)
    print(person)
except (InvalidNameException, InvalidAgeException) as e:
    if e.error_code==10:
        print("Invalid Name")
    elif e.error_code==5:
        print("Invalid Age")
    else:
        print("Something else went wrong")
    
print("Hello World")

'''
Invalid Name
Hello World
'''