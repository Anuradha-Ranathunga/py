class Dog:
    pass

dog1 = Dog()

dog1.name= "Shaggy"
dog1.breed= "Labrado"

dog2 = Dog()

print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)

#Output => AttributeError: 'Dog' object has no attribute 'name'