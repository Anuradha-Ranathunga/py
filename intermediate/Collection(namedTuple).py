import collections
from collections import namedtuple

#can access things by using elements

Point1 = namedtuple('Point2' , 'x  gy z h') #namedtuple is new object and name of the tuple is 'Point2'
# we will treat this like a class

newP = Point1(3,4,5,8)
print(newP)

###############################################################

Point = namedtuple('Point', ['x','y','l'])
newP = Point(3,4,5)
print(newP)

###############################################################

Point = namedtuple('Point',{'x':0 ,'y':0 ,'z': 0})
newP = Point(3,4,5)
print(newP.x , newP.y , newP.z)
print(newP)
print(newP[0])
print(newP._asdict())
print(newP._fields)

print(newP._replace(y=6))

p2 = Point._make(['a', 10, 'c'])
print(p2)

