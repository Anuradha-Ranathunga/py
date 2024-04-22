x = 10

#indentation =  Idiriyen ati his than ganana. Block(:) ekakata pasuwa his than 4k thiyenna one

if x >= 150:
    print("You're selected!")  
else:
    print("You're not selected.")  
    
marks = 75
result = ""
if marks>50:
    result= "Pass"
else:
    result= "Fail"
    
print (result)

#Without subsection

marks = -76
if marks>=0 and marks<35:
    print("W")
elif marks>=35 and marks<55:
    print("S")
elif marks>=55 and marks<65:
    print("C")
elif marks>=65 and marks<75:
    print("B")
elif marks>=75 and marks<=100:
    print("A")
else:
    print("Invalid")
    
height= 176
#method 1
if height>150:
    job = "Security"
else:
    job = "Labor"
    
print(job)

#method 2
job= "Security" if height>150 else "Labor"
print(job)

#method 3 - ternary operator(3 parts -  condition,true part, false part)
msg = "Your job is "+ ("Security" if height>150 else "Labor")
print(msg)
