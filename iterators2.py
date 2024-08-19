class MyNumbers:
    def __init__(self, x):
        self.x = x
        
        
    def __iter__(self):
        self.a = self.x
        #self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return self.a

myclass = MyNumbers(2)
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))