from os import path

file_name = '26data1.txt'

x = 10
y = 1

try:
    z= x/y
    print(z)
    
    #can get FileNotFound Error
    with open(file_name) as file:
        print(file.readlines())

except Exception:
    print("Something went wrong.")
       
except ZeroDivisionError:
    print("Input Error")

except FileNotFoundError:
    print("File Not Found")
    
'''
10.0
Something went wrong.
'''
#exception yanu generic exception ekak nisa siyalu errors exception magin catch kara ganee.
#E nisa exception mulin thibu wita eya magin errors catch karagena pahala line walata ewa laba nodeyi.    
#e nisa generic exception awasanayata danawa. 
#specific exceptions mulin danawa. 


