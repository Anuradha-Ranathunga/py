x = [12,23,567,123,88]

for item in x:
    print(item) 
    print(type(item))
    
            #method 1
index = 0

for item in x:
    y = x[index]
    print(index, y)
    index += 1
    
            #method 2
for item in enumerate(x): #mehi item eke type eka tuple ekak we. because enumerate function eken hama witama index eka saha ita adala value eka return karayi.
    index = item[0]
    value = item[1]
    print(type(item), item)
    print(index,value)
    #item is a tuple => (0,12) (1,23) (2,567) (3,123) (4,88) So item[0] means 0,1,2,3,4 and item[1] means 12,23,567,123,88
    print(item)
    
            #method 3
for index, value in enumerate(x):
    print(index,value)
    
            #method 4
for item in enumerate(x):
    index, value= item
    print(index,value)
    
            #nishchitha wara gananak loop eka run kara ganimata
#we will use range function for that and we need to provide 2 parameters as starting value and end value

s= range(0,len(x))
for item in s:
    print(item) #this item means not a list's item. it is range's item. Enam mehidi pring wenne value neme. List eke length ekata anuwa index print wenawa
    print(x[item]) #item is act as a index here
    
r = range(0,10)
print(type(r))
for item in r:
    print(item)
    
    
#for item in range(0, 10): #10 is exclude- 10 athulath nowe
    #print(item)
    #print(type(item))