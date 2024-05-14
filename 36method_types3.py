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
        #print(cls)
    
        
Anu = Person("Anu")
Anu.print_name()

print(Person.get_types())

'''
Person is created.
<__main__.Person object at 0x00000211493765D0>
Name :  Anu
['Student', 'Teacher', 'Librarian']
'''
#class method ekedi instance variable walata or instance function walata kisidu access ekak na. 
