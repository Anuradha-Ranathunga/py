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
            print("Error") #raise karama line 12 walin program eka crash wenawa. ethakota pahala line run wenne na. 
        
        if age<0 or age>120:
            raise Exception("Invalid age")
            return
        
        return Person(name, age)

#create object        
person =Person.get_person("" , -23)
print(person)

'''
Traceback (most recent call last):
  File "c:\Users\Anuradha\Desktop\Python\39custom_excep4.py", line 22, in <module>  
    person =Person.get_person("" , -23)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\Anuradha\Desktop\Python\39custom_excep4.py", line 12, in get_person
    raise Exception("Invalid Name")
Exception: Invalid Name
'''