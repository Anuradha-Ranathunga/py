#class eke thiyen attribute witharak define karanna function ekak create karanna one. 
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
    def get_types(x):
        print(x)
    
        
Anu = Person("Anu")
Anu.print_name()

print(Person.get_types())

'''
Person is created.
<__main__.Person object at 0x000001E51C9D6540>
Name :  Anu
<class '__main__.Person'>
None
'''

#normally define karana function ekaka palaweni parameter eka=> Relevant object
#@classmethod yana decprator eka dala hadana function wala palaweni parameter eka=> name of the class