#Instance functions/ instance methods
class Person:
    
    types = ['Student' , 'Teacher' ,'Librarian'] #function eken eliye hadana attribute => Class attribute
        #class attributes=> class eka haraha access karanna puluwan. intance haraha access karanna awashya na. 
    def __init__(self,name):
        print("Person is created.")
        self.name= name
        
    def print_name(self):
        print("Name : ", self.name)
        
Anu = Person("Anu")
Anu.print_name()

print(Anu.name)
print(Anu.types)
print(Person.types)

'''
Person is created.
Name :  Anu
Anu
['Student', 'Teacher', 'Librarian']
['Student', 'Teacher', 'Librarian']
'''