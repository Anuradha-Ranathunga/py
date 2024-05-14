class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 25 #class ekak athule me widiyata define karala thiyenawa nam eka pitathin access karanna ba. 
   
   #age variable ekata value ekak assign kireema
    def set_age(self,age):
        self.__age = age
    
    #age variable eke value eka pitathata return kara ganimata.          
    def get_age(self):
        return self.__age
        
    def sleep(self):
        print("Sleeping...", self.name)
        
Anuradha = Person("Anuradha")
Anuradha.sleep()
Anuradha.set_age(30)
Anuradha.__age= 50 #me line 19 thiyenne line 4 thibba variable eka neme. meka wenama variable ekak hadanawa __age kiyala.
print("Name is ", Anuradha.name)
print("Age is ", Anuradha.get_age())
print("Age is ", Anuradha.__age)

'''
Sleeping... Anuradha
Name is  Anuradha
Age is  30
Age is  50
'''
#mema getters and setters yodagena class eke thiyena private variable hinde karanna puluwan. => encapsulation