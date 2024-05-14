#modules

name = "Anu"

def get_name():
    print(__name__) #person file eke module name eka
    print(__file__) #person file eke sampurna path eka laba ganna puluwan. 
    return name

def get_age():
    return 50

#mema function deka class ekak athule define karala nathi nisa self awashya wenne na. 

if __name__ =='__main__':
    print("This is the entry point")
