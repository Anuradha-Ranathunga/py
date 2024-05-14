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
    
    @staticmethod #object eke thiyena attribute and class eke thiyena attribute access karanna ba. 
    def get_person():
        return Person()
    #@Static method=> normal function ekak, speciality eka wenne class ekata kisidu sambandayak nathuwa use karanna puluwan.
    #meka object eka through menma class eka through da call karanna puluwan.    
    #class eka athulata function ekak widiyata danna puluwan. But eka class eke object walin and class eken independent.
        
Anu = Person("Anu")

p = Person.get_person()
print(p)
print(p.name)
#Aluthin object create kireema sadaha da @staticmethod use karanna puluwan

'''
Person is created.
Person is created.
<__main__.Person object at 0x00000131168469F0>
Unknown
'''