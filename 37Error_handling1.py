from os import path

file_name = '26data1.txt'

if path.exists(file_name):

    #can get FileNotFound Error
    with open(file_name) as file:
        print(file.readlines())

else:
    print("File does't exist")

'''
File does't exist
'''