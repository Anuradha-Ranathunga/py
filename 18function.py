#method 1
'''
def get_grade(): #create function
    print("Hello")

get_grade() #call the function

marks_list  = [78,67,46]

for marks in marks_list:
    if marks < 0  or marks > 100:
        print("Invalid")
    elif marks<35:
        print("W")
    elif marks<55:
        print("S")
    elif marks<65:
        print("C")
    elif marks<75:
        print("B")
    else:
        print("A")
'''

#method 2
'''
def get_grade():
    if marks < 0  or marks > 100:
        print("Invalid")
    elif marks<35:
        print("W")
    elif marks<55:
        print("S")
    elif marks<65:
        print("C")
    elif marks<75:
        print("B")
    else:
        print("A")

marks = 75
get_grade()

marks = 54
get_grade()
'''

#method 3
'''
def get_grade(marks):
    if marks < 0  or marks > 100:
        print("Invalid")
    elif marks<35:
        print("W")
    elif marks<55:
        print("S")
    elif marks<65:
        print("C")
    elif marks<75:
        print("B")
    else:
        print("A")

get_grade(75)
get_grade(54) #when we pass the values, it should match to the logic. Ex. If we pass String, then output is an error. 
'''

#using 2 argumemts
'''
def get_grade(subject, marks):#Positional parameters=> Value is define according to the position
    print("Subject = ", subject)
    if marks < 0  or marks > 100:
        print("Invalid")
    elif marks<35:
        print("W")
    elif marks<55:
        print("S")
    elif marks<65:
        print("C")
    elif marks<75:
        print("B")
    else:
        print("A")

get_grade("Sinhala" , 75)
get_grade("Maths", 54)

#If we have 2 parameters we should able to pass the 2 arguments
'''

#create optional parameters using default values
'''
def get_grade(marks, subject= "Unknown"): #default argument => Default arhument ekak thiyen parameter ekakata passe default argument ekak nathi parameter ekak danna ba. 
    print("Subject = ", subject)
    if marks < 0  or marks > 100:
        print("Invalid")
    elif marks<35:
        print("W")
    elif marks<55:
        print("S")
    elif marks<65:
        print("C")
    elif marks<75:
        print("B")
    else:
        print("A")

get_grade(75)
'''

#named arguments
def get_grade(marks, subject= "Unknown"):
    print("Subject = ", subject)
    if marks < 0  or marks > 100:
        print("Invalid")
    elif marks<35:
        print("W")
    elif marks<55:
        print("S")
    elif marks<65:
        print("C")
    elif marks<75:
        print("B")
    else:
        print("A")
        
get_grade(marks=75, subject="Sinhala")# <= named arguments- when we forgot the parameter order.
#Even if there is a one named arguments, all other arguments which is in the right side must be named arguments
#named arguments serama right side eke kelaware thiyenna one. 
#Ex. get_grade(75, subject="Sinhala") 
#named argument ekakata passe positional arguments enna ba. But positional argument ekakata passe named argument ekak thiyenna puluwan. 
