from collections import Counter

c = Counter(a = 4, b=2 , c = 0 , d = -2)
d = Counter(['a', 'b' , 'b' , 'c'])

#print(c)
#c.update(d)
#print(c)
#c.clear()
#print(c)

print(c+d)
print(c-d)

print(c & d) #intersection
print(c | d)

#print(list(c.subtract(d)))