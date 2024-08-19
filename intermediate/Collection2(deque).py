import collections
from collections import deque

d = deque("hello" , maxlen=5)
print(d.maxlen)
#d.maxlen = 5 => can't add maxlen like this. bcz there will be an error
print(d)
#d.append(1)
#print(d)

d.extend([1,2,3])
print(d)