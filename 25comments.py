#this prints hello world
print("Hello World")

"This is another awesome string"
#String value variable ekakata assign karala nattam or eka use karala nattam eka automatically ignore karala danawa. 

def my_func(x,y):
    """
    This is my first comment
    this is my second
    @param x: first number
    @param y: second number
    @returns: multiplication of x and y
    """
    return x*y

#multiline comments=> doc string - function ekaka documentation eka. e magin function ekak wisthara karanawa. (ex. Epytext or Epydoc )

my_func("anu",10)

    #3.Type hinting => function ekaka description eka thawath wadi karanna use karanawa.'
def my_func(x : int , y: dict):
    """
    
    
    """ 

#default value daddi
def my_func(x : int=None, y: dict= None)-> int:
    """
    
    
    """ 
    
#TODO: Change this some other time
a = my_func("text" , 5)

#BUG:
#FIXME:

"""
2 type of comments.
    1.single line comments (#)
    2.multi line comments 
            1- ''' - '''
          
            2- doc string=> function ekaka paramters and return wenne mokadda kiyala explain karanawa.
             ctrl+space=> documentation eka bala ganna puluwan
            
            3- type hinting => dana parameters wala and return type eke data type eka bala ganna puluwan.
            meka interpreter eken process karanne na. e nisa waradi data type pass kara kiyala intepreter complain karanne na.
            code eka kiyona kenata terum ganna udau wenawa.   
            
            
        


"""
