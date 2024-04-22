
x = {1: 'A', 2: 'B', 3: 'C'}

#y =  x[5] => Dic eke nathi value ekak illaddi meka crash wela error ekak pennayi. 
y = x.get(4,0) #key = 4 ta adala value eka denna. eka nathnam 0 return karanna.

z = x[1]



print(y)
print(z)


#pass by reference

x= {
    "a": ['Hello' , 'Hi' , 'Good morning'],
    "b": ['Bye', 'Good night']
}

y= x['a']
y.append('Aayubowan')

print(y)
print(x)
