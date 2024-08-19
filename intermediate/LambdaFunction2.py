a = [1,2,3,4,5,6,7,8,9,10]

newList = list(map(lambda x : x + 5 , a))
print(newList)

newList2 = list(filter(lambda x : x%2 == 0, a))
print(newList2)