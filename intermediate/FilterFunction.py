def add7(x):
    return x + 7 

def isOdd(x):
    #return x%2 != 0 
    #return True
    #return False
    return 'hi'
    
a = [1,2,3,4,5,6,7,8,9,10]
print(a)

b = list(filter(isOdd , a ))
print(b)

c = list(map(add7, filter(isOdd , a )))
print(c)