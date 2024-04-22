x = {'1000':"Colombo", "12500":"Panadura"}
x['1200'] = "Moratuwa"
print (x)
print(x.keys())
print(x.values())
x['Cities'] = ['Kaluthara', ' Malabe'] #insert list
x['values'] = {1 : '6543', 78 : '54678'} #insert another dictionary

#dictionary index magin access karanna ba. Because mewa insert karana order ekatama store wenne na. 
#But apita adala key eka magin access karanna puluwan. 
#Dictionary wala value ekata ona taram complex dewal danna puluwan.But key eka ekama type eken dana eka hodai.

x[0]= "Zero"

y= x[0]
del x['Cities']

x.clear()
print(x)


print(y)


b= x['1000']
print("Hello " , b) #We will get an error.Because We cleared this dictionary previously in the line 18



