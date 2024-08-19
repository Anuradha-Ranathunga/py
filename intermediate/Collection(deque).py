import collections
from collections import deque

#deque is faster than lists when adding elements in the beginning and the end
d = deque("hello")
print(d)
d.append('4')
d.append(5)
d.appendleft(7)
print(d)
d.pop()
print(d)
d.popleft()
print(d)

d.clear()
print(d)

d.extend('456')
print(d)

d.extend('hello')
print(d)
d.extendleft('hey')
print(d)

d.rotate(-2)
print(d)


