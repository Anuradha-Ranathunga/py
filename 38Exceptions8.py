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
    
except ZeroDivisionError as e:
    print("Input Error" , e)

except FileNotFoundError as e:
    print("File Not Found" , e)
    
except Exception as e:
    print("Something went wrong." , e)
    
finally:
    print("Process completed")
    
'''
10.0
File Not Found [Errno 2] No such file or directory: '26data1.txt'
Process completed
'''