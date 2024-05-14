from os import path #from => parent module , import => child module

import module_person1

if path.exists('module_person1.py'):
    print("Person is there")
    
'''
Person is there
'''