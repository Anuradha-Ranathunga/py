#from os import path #from => parent module , import => child module
import os.path as path #this is called as Alias, module eke nama diga wadi weddi e wenuwata temperary keti namak yoda ganiyi. 

import module_person1

if path.exists('module_person1.py'):
    print("Person is there")
    
'''
Person is there
'''