x = ['a','b','c','d']

#y=[]
#y.append(x[0])
#y.append(x[1]) mema method ekada me sadaha yoda gatha haka. namuth meka practically apahasuyi elements godak add karanna awashya wuna wita

# slicing = list eke data extract kara ganimata
y = x[0:2]
z = x[2:3]
w = x[2:4]
u = x[2:10]
a = x[2:]
b = x[:2]
c = x[-1] #antima element eka ara ganna. 
d = x[:-1] #anthima element eka hara ithiri tika print kara ganimata

print(y)
print(z)
print(w)
print(u)
print(a)
print(b)
print(c)
print(d)
#mema slicing method eka list and tuples walata pamanak adala weyi. dictionary and set walata meka ayath nowe. because dic and sets index walin access karanna ba.

#length
print(len(y)) 

#Strings wuwada apita slice karanna puluwan
e = "HELLO WORLD"
f = e[0:-1]
print(f)
print(e[6])

#Summery of Data Structures
# x = [] - list
# y = {"1": 1} -  Dictionary / Key-value pair
# z = {"1","2"} -Sets
# a = ("1", 12, True) - Tuple

# b = "HELLO WORLD" - This is also list of characters
