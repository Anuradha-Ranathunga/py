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
        cls.print_name() #error ekak display wenawa
        return cls.types
        
        #print(cls)
    
        
Anu = Person("Anu")
Anu.print_name()

print(Person.get_types())

'''
Person is created.
<__main__.Person object at 0x000002542D356630>
Name :  Anu
['Student', 'Teacher', 'Librarian']
PS C:\Users\Anuradha\Desktop\Python> & C:/Users/Anuradha/AppData/Local/Programs/Python/Python312/python.exe c:/Users/Anuradha/Desktop/Python/36method_types4.py       
Person is created.
<__main__.Person object at 0x0000016387506630>
Name :  Anu
Traceback (most recent call last):
  File "c:\Users\Anuradha\Desktop\Python\36method_types4.py", line 25, in <module> 
    print(Person.get_types())
          ^^^^^^^^^^^^^^^^^^
  File "c:\Users\Anuradha\Desktop\Python\36method_types4.py", line 16, in get_types
    cls.print_name()
TypeError: Person.print_name() missing 1 required positional argument: 'self'  
'''