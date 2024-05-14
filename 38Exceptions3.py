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
    
except ZeroDivisionError:
    print("Input Error")

except FileNotFoundError:
    print("File Not Found")
    
except Exception:
    print("Something went wrong.")
    
'''
10.0
File Not Found
'''