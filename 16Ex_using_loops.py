#x = [-12,-23,-567,-123,-88]
"""
#using for loop
#find total and average
total = 0

for i in x:
    total+=i
    
print("Total ",total)
print("Average ", total/len(x))
"""
"""
#maximum number and minimum number of the list
max = 0
for i in x:
    if max<i:
        max=i
print("Max ", max)# if all the numbers which is in the x list are negative numbers, then our final output is 0. 
                  #But we want to get the maximum number by only considering the x list. 0 is not in the x list. Then it is wrong.
"""
"""
#We can use following method to recover the mentioned issue.

max = x[0]
min = x[0]
for i in x:
    if max<i:
        max=i
    if min > i:
        min = i
        
print("Max ", max)
print("Min ", min)
"""

#using while loop
#total and average of the number list
x = [12,43,67,356,76,45]

count = 0
total = 0

while count<len(x):
    item = x[count]
    total += item
    count+=1
    
print("Total ",total)
print("Average ",total/len(x))

#minimum and maximum number of the list
min = max = x[0]
count=0

while count<len(x):
    item = x[count]
    
    if item > max:
        max = item
    
    if item < min:
        min = item
    
    count+=1

print("Max ",max)
print("Min ", min)