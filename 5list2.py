x = {
    "a" : ['Hello', 'Hi', 'Good Morning'], #list is not a basic data type. Eke pointer eka or memory address eka return karanu labayi. 
    "b" : ['Bye' , 'Good night'],
    "c" : 65 #this is basic data type. Z ta assign wenne eke copiyak 
}

y = x['a']
y.append('Aayubowan')
print (y)
z = x["c"] 
#x['a'] gen return une list ekaki. But x['c'] eken basic data type ekak return wena nisa eke copiyak z ta assign wenawa. 
# Ema nisa z ta karana wenaskam x ta balapanne na. 
#But list is not a basic data type. Eken return wenne pointer(memory address) ekak. 
#Ewita y ta karapu siyalu changes x tath balapanawa. 
z= 17
print(x)