'''
def  get_grade(marks, subject=None):
    
    if not subject:
    #if subject=="Health":
        print("Health is not in the scheme.")
        return
    
    #print("Subject ", subject)
    if marks < 0  or marks > 100:
        #print("Invalid")
        return None
    elif marks<35:
        return("W") #return => Nawatha value ekak eliyata yawanna.
    elif marks<55:
        return("S")
    elif marks<65:
        return("C")
    elif marks<75:
        return("B")
    else:
        return("A")
    
    print ("Hello")

grade = get_grade(75)   
#grade = get_grade(-75, subject= "Health")   
#grade = get_grade(75, subject= "Sinhala") #value eka return karama eka print wenne na. but eka call karapu kena wetha gaman karanawa. 
#grade = get_grade(-75, subject= "Sinhala")
if grade:
    print("Grade ",grade)
else:
    print("Something went wrong")

#print(grade) #function ekakin kisiwak return kare nattam eka authomatically 'None' kiyala hithanawa. 

#Return eken passe function eka athule kisiwak run wenne na. 
#Return ekath ekka value ekak athuwa or nathuwa return karanna puluwan. 
'''
'''
def  get_grade(marks, subject=None):
    
    #print("Subject ", subject)
    if marks < 0  or marks > 100:
        grade= None
    elif marks<35:
        grade = "W" #return => Nawatha value ekak eliyata yawanna.
    elif marks<55:
        grade= "S"
    elif marks<65:
        grade= "C"
    elif marks<75:
        grade = "B"
    else:
        grade = "A"
    
    print ("Hello")
    return grade 

grade = get_grade(75)
if grade:
    print("Grade = ", grade)
else:
    print("Something went wrong!")
'''
    
    #mewayin values 2,3 wuwada return kara gatha haka. 
def  get_grade(marks, subject=None):
    
    #print("Subject ", subject)
    if marks < 0  or marks > 100:
        grade= None
    elif marks<35:
        grade = "W" #return => Nawatha value ekak eliyata yawanna.
    elif marks<55:
        grade= "S"
    elif marks<65:
        grade= "C"
    elif marks<75:
        grade = "B"
    else:
        grade = "A"
    
    print ("Hello")
    return subject , grade #function ekakin values kipayak wuwada return karanna puluwan. ewa return wenne tuple ekak widiyata. 
#grade = get_grade(75, "Science")
subject, grade = get_grade(75, "Science")
#print(type(grade) , grade)
print(type(grade), subject , grade)

if grade:
    print("Grade = ", grade)
else:
    print("Something went wrong!")