'''
def is_odd(number):
    if number%2 ==1:
        return True
    else:
        return False
    #istead of 2,3,4,5 lines=> return number%2 ==1
    #ternary operator => return "Odd" if number %2==1 else "Even"
    
a = [12,45,85,87,33]

b = a 
# a ta karana siyalu changes b tath apply wenawa.
# a and b yana variable dekama ekama list object ekata point karanawa. 

        #generate another list from a list
b = list(a)

        #generate another list from a list using for loop
b = []
for i in a:
    b.append(i)


        #generate another list from a list using list comprehension

b = [i for i in a] #a gen i labagena eka b ta return karanna. If you want you can do any changes
# ex. b = [1*2 for i in a]


b = [is_odd(i) for i in a ]


b.append(100)

print(a)
print(b)
'''

#Use logic for a list comprehension
def is_odd(number):
    return "Odd" if number % 2 == 1 else "Even"

a = [12,45,85,87,33,100,34, 11]
b = []


  
b = [is_odd(value) for i,value in enumerate(a) if i%2==0] #dan inna index eka hoya ganna enumerate use karayi.
#for loop eka run karana gaman if condition eka check karanna. eka true nam function eka evaluate karanna. 

print(b)
#If you want you can get dictionary also.
b = [{value : is_odd(value)} for i,value in enumerate(a) if i%2==0]
#or we can put in the line 42 => return {value :"Odd"} if number % 2 == 1 else {value:"Even"}

#Kalin awe dictionary include una list ekak(dictionary list). if you need you can get dictionary by including dictionaries.
b = {value : is_odd(value) for i,value in enumerate(a) if i%2==0}
#value=> key ,  is_odd(value)=> value

print(a)
print(b)

'''
#Put that same logic using loop
for i,value in enumerate(a):
    if i%2==0:
        r=is_odd(value)
        b.append(r)  
    
print(a)
print(b)
'''

#When we generate list => list comprehension
#when we generate dictionary => dictionary comprehension

#generate set comprehension
b = {value for i,value in enumerate(a) if i%2==0}
print(b)

#generate tuple comprehension
b = (is_odd(value) for i,value in enumerate(a) if i%2==0)#This is generator. We can print it using the following codes.

for i in b:
    print(i)