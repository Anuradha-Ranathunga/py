class Person:
    
    types = ['Student' , 'Teacher' ,'Librarian'] 
    def __init__(self,name):
        print("Person is created.")
        self.name= name
        
    def print_name(self):
        print(self)
        print("Name : ", self.name)
        
    #class attribute witharak use karanna awashya wena wita=> class methods (decorator)
    #decorator=> function ekakata wadi wistharayak denna meya yoda ganiyi. 
    @classmethod
    def get_types(cls):
        return cls.types
        
    
        
Anu = Person("Anu")
Anu.print_name()

Person.print_name(Anu)

print(Person.get_types())

'''
Person is created.
<__main__.Person object at 0x000001C938F76660>
Name :  Anu
<__main__.Person object at 0x000001C938F76660>
Name :  Anu
['Student', 'Teacher', 'Librarian']
'''

'''
instance method=> Palaweni parameter eka lesa object eka automatically pass wenawa. 
class method=> palaweni parameter eka leda class eka automatically pass wenawa. 

'''