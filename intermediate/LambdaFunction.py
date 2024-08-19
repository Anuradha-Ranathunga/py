'''
def func(x):
    return x +5 

func2 = lambda x: x + 5 
print(func2(9))
print(func(2))
'''
def func(x):
    func2 = lambda x : x+5
    return func2(x) + 85

func3 = lambda x,y=4 : x+y
print(func3(5,5))
print(func3(5))

print(func(2))

