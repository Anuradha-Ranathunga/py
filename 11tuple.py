#tuple
# list - [] , set and dictionary {}  , tuple ()
anuradha = ("Anuradha", 156, "Sri Lanka")

print(type(anuradha)) #various type wala data set group kara ganna widiyak
#in the data base, 1 row= 1tuple
print(anuradha)#anuradha is name of the variable

name= anuradha[0]
print(name)
print(anuradha[0])
#tuple wala data remove karanna ba. iwath karanna one nam list ekakata convert karala ita passe iwath karanna wenawa
print(anuradha[1])
print(anuradha.count("anuradha"))#mehi elements ganana count karanna puluwan
print(anuradha.count("Anuradha"))#Anuradha value eka kiparak tuple eka athule thiyenwada kiyala balayi

#tuple wala athi values wena wenama variable walata assign karanna puluwan
x = (1, "Anuradha" , 156)
index , name ,height =x
print(type(x),x) #x ge type eka saha x print kara ganimata. 
print(index,name, height) #tuple eka value walata convert karanawa= expand the tuple
#mehi values 3, variable 3ta assign karanu labayi. But values 3, variables 2 kata assign kalahoth "too many values to unpack" lesa error ekak penwayi.
#index, name= x
#print(index, name) 
index = x
print(index) #if you need, variabale eka thawath eka variable ekakata ssign kara melesa tuple eka print kara ganna puluwan
