x = [12,23,567,123,8]

#max = x[0]
#min = x[0]
"""
count = 0

while count<10:
    print("count", count)
    count+=1
  
for i in x:
    if i>=100:
        break
    print(i)

    
#infinite loop
count=0
while True:
    
    if count==15:
        break
    
    print("Count", count)
    count+=1
"""
   
#continue =  Skip the relevant iteration
count = 0

for i in x:
    if i % 2 ==0:
        continue
    print(i)
    print(i**2)


count=0    
while True: # or while count ==len(x)-1: break => If we use this condition for a while loop instead of True, we can remove 43,44 line from the code.
    print("Index", count)
    
    if count== len(x)-1:
        break
    
    i=x[count]
    if i%2 ==0:
        count+=1
        continue

    print(i)
    print(i**2)
    count+=1
