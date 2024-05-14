#from os import path #from => parent module , import => child module
import os.path

import module_person1

if os.path.exists('module_person1.py'):
    print("Person is there")
    
    
'''
Person is there
'''