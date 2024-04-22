x = {"Hello" , "World" , "Hello" , "1" , "1"}
y = {"1", "2"}

#z = x+y - wrong one

#z= x.union(y) - union operator (correct one) 

z = x | y #pipe operator (this is also correct) => sets dekak ekathu karanna yoda ganiyi. 
a= x-y #y wala athi siyalu element x gen ayin karayi
print( "1" in y)
print("1" not in y)

b = {"1": 2} #dictionary
print("1" in b) #dictionary walatath meka correct
print("2" in b) 
#dictionary waladi "in" walin check karama eka balanne key eka athule, value eka athule neme.
print(a)
print(z)
