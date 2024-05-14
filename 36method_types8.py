class Person:
    
    types = ['Student' , 'Teacher' ,'Librarian'] 
    def __init__(self,name="Unknown"):
        print("Person is created.")
        self.name= name
        
    def print_name(self):
        print(self)
        print("Name : ", self.name)
        
    @classmethod
    def get_types(cls):
        return cls.types
    
    @staticmethod  
    def get_age(today, dob):
        return today - dob
    
Anu = Person("Anu")

p = Person.get_person()
print(p)
print(p.name)

'''
            3 type of methods
1. instance methods=> palaweni parameter eka(object eka) automatically pass wenawa.
2. class method =>  palaweni parameter eka automatically class eka pass wenawa.
3. static method => automatically kisidu parameter ekak pass wenne na. 

'''