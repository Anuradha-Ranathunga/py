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
    
except (ZeroDivisionError, FileNotFoundError): #mema errors deken ekak ho sidu wu wita mema line eka run karanna.
    print("Input Error")

    
except Exception:
    print("Something went wrong.")
    
'''
10.0
Input Error
'''