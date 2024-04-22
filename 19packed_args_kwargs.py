
def get_grade(*marks):
    print(type(marks))
    total = 0
    for i in marks:
        total +=i
    
    print(total)

#m = [78,75,43] #this is list
#get_grade(m) #pass the 1 value
            
            #use packed arguments
get_grade(78,75,43) #pass the 3 arguments. Then it will crash. For avoid that we will use packed arguments.
#packed args =>Api dana arguments pramanaya anuwa parameters pramanaya wenas wenawa. It is define using * front of the variable
#siyalu arguments ekathu karala thani tuple ekak hadala yawana eka packed argument walin karayi. 
#This packed argument is use for pass the variable number of arguments pass to the function. 
#ex. print function => If we provide any number of inputs or 0 input, all of them are print using that print function. Packed argument is similar to the print function.


                #kwargs arguments

#Ex. Web APIs
def my_form(**params):
    if 'name' not in params:
        print("Error")
    else:
        print("Hello ", params['name']) #dictionary wala values access karanna puluwan eke key eka dila. 
    print(params)

my_form(height=156 , city = "Gampaha")
my_form(name ="Anuradha" , height=156 )
#arguments ganan wadi wana wita parameter define karanna amaru nisa saha data enter kirimedi thiyena combinations walata anuwa default value set kirima apahasu nisa => kwargs yoda gani
#kwargs  args => **(name of the parameter)
#keyword argument magin mehidi laba dena siyalu argument ekak ma dictionary ekakata convert karala laba gani. Dic =>keyword argument walata convert karannatath meya yoda gani. 
#function eka awashya paridi customize kara ganna meka udau wenawa.

#packed arguments ekka dekama ekata use karanna puluwan. But mulin packed args thibiya yuthuyi. 
#Keyword args piti passe thiyenna one. Because packed args is positional arguments. E nisa positional args mulin thiyenna one. named args one thanaka thiyenna puluwan. 


        #packed and kwargs arguments
def my_form(*values , **params):
    print(type(values))
    print(type(params))
    print(values)
    if 'name' not in params:
        print("Error")
    else:
        print("Hello ", params['name']) #dictionary wala values access karanna puluwan eke key eka dila. 
    print(params)

my_form(1, 78, height=156 , city = "Gampaha")
my_form(name ="Anuradha" , height=156 )

#function ekak define karaddi positional args and named args yoda gani. So packed args and kwargs args bawitha karanawa nam 
#Aniwaren packed args mulin thiyenna one. kwargs args/named args passe thiyenna one. 
    #packed args => Optional args - we can use various number of argumemts => Tuple (*values)
    #kwargs args => named args - we need to provide name of the argument and don't need to provide defalt values => Dictionary (**params)
    
        #convert dictionary into named argument
def my_form (name, height): #def my_form (**name) - named args convert into dictionary
    print(name, height) 

#create dictionary   
#arguments define karaddi name, height wala quotations danna wenawa. because it is dictionary.
#other wise there will be a syntax error. 
#Then dictionary eka parameter ekata pass karanna one. 
args = {
    'name': "Anuradha",
    'height' :  176
}

my_form(name = "Anuradha" , height=176) #name and height are names of the parameter
my_form(**args) #my_form(args ) is wrong. because name parameter eka argument ekata assign kara ganna nisa. 
                #we can expand the arguments using **.function  eka call karaddi ** dammoth adala dictionary eka named args bawata convert wenawa. 
#if def my_form(name. height,city) => then there will be an error. because city parameter ekata adala value ekak dictionary eke pass karala na. 

#pass karana argument set eka(line 69) dila thiyena parameter set ekata(line 62) match wenna one. 

#value pass karaddi digata line eka dige value pass karana eka (line 74) amaru nisa adala value dic ekakata dala ita passe named args bawata convert karala (line 75) parameter ekata assign karayi. 
