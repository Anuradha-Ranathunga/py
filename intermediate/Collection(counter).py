import collections
from collections import Counter

'''
        Containers
list
set
tuple
dict

        Types
1  counter
2  deque
3  namedTuple
4  orderdDict
5  defaultdict
'''

c = Counter('gallad')
print(c)
c = Counter(['a', 'a', 'b', 'c' , 'c'])
print(c)
e = Counter({'a':1, "b":2})
print(c)
d = Counter(cats = 4, dogs = 7)
print(c)
print(c['cats'])
 
print(list(c.elements()))

print(c.most_common(2))


