            #iterate dictionary

d = {
    "anuradha": 176,
    "saman" : 167,
    "saranga": 150,
    "siri" : 160
}
"""
for i in d:
    print(i) # mehidi print wenne keys pamanayi. 
"""
    
#print the value in the dictionary
"""
            #method 1
for name in d:
    height = d[name]
    print(name, height)
"""
'''    
            #method 2
for name,height in d.items(): 
    #d.item function => dictionary wala athi item yana function eken return wenne key and value ekathu karapu tuple ekaki. 
    # e tuple eka variable 2kata assign kara gannawa. 
    
    print(type(name))
    print(name)
#name is a tuple. Tuple ekata ena values apita expand kara ganna puluwan variables walata. 
    print(name,height)
    
            #method 3
for i in d.items():
    name, height=i
    print(i)
    print(name, height)
'''
            #method 4 => using enumerate function
for i,x in enumerate(d.items()):
    print(i,x) # As a output i is index. But x is tuple
#for i, name, height enumerate(d,items()): => when we add this code for expand the tuple, we will get an error.
#because enumerate function is provide only 2 values. These are index and tuple which is including key and value.
    name, height = x
    print(i, name , height)
  
            #iterate sets

s= {
    "Anuradha",
    "Saman",
    "Sajith",
    "Siri"
}
  
'''
    #method 1
for name in s:
    print(name)
'''

'''
    #method 2
for i, name in enumerate(s):
    #x=d[i] => we can not access set using index
    #But using i we can easily chech which itereation is in now
    print(i, name)

'''

            #iterate tuple
'''
t = ("Praneeth", 176, "Panadura", "Sri Lanka")

for i, name in enumerate(t):
    print(name)
    print(i, name) #i => index
'''