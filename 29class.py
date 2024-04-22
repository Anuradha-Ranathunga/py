class MyFirstClass: #hama wachanema mul akura capital, spaces thiyanne na
    #pass #content ekak noda skip karanawa. danata implement karana na kiyana eka mean wenawa
    name = ""
    breed = ""
    
    def bark(self, message):
        #print(type(x),x)
        print("Inside ", self)
        print("Woof Woof ", message )

#class=> mokak hari entity ekaka bluprint/plan
dog1 = MyFirstClass() #create object #dog1=> instance
print("Outside ", dog1)
dog1.name= "Shaggy"
dog1.breed="Labrado"

dog2 = MyFirstClass()

print(dog1.name, dog1.breed)

print(dog2.name, dog2.breed)

#dog1.bark() #class ekak athule object ekak haraha function call karana wita python automatically dog1 kiyana eka argument ekak widiyata pass karanawa. => dog1.bark(dog1)

#class ekakin hadapu instance ekaka(object ekaka) function ekak call karoth python automa eke palaweni argument eka widiyata e object ekama pass karanawa.
#class eka athule function ekak define karanawa nam e function eke eka paramter ekak aniwaren by default liyanna one. 
#palaweni parameter eka normally self kiyala danawa. 
dog1.bark("Hello") #methana argument dekak thiyenawa. palaweni eka object eka, deweni eka msg eka. 



