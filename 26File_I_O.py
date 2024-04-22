'''
main modes in the python

'r'  =read only
'w'  =write with truncate
'x'  =open for exclusive creation
'a'  =append
'b'  =binary
't'  =text mode
'+'  =updating

'''     

#hard disk eke save karala thiyena file python walin read karanna thiyena inbuild function=> open
'''
file = open("26data.txt") #file eke thiyenne computer eke wena thanaka nam eke path eka denna one

print(type(file))

#contents = file.read(5) #read the contents
                        #parameter- kochchara data read karanna oneda kiyala
                        #parameter ekak dunne nattam mulu file ekama read karapu nisa storage eka wadi unoth meka overflow wenna puluwan

#using while loop
while True:
    
    contents = file.readline() #read the line by line
    if not contents:
        break
    
    print(contents)

#using for loop
for line in file:
    print("Line--> ", line)

#or
for i,line in enumerate(file):
    print("Line-->" ,i,line)
    
#file eka use karanna hadapu open eka eka use karala iwara unama close karann one
file.close()

'''
'''
x = ['1','2','3','4']

msg= ','.join(x)
print(msg)
'''
'''
file = open("26data.txt",'w')

#msg= ','.join(range(0,100)) #meka string walata convert kara ganna one

x = [str(i) for i in range(0,100)]
msg = ', ' .join(x)
msg1 = '\n'.join(x)


file.write(msg)
file.write(msg1)

file.close()
'''

'''
file = open("26data.txt",'w')

for i in range(0,100):
    file.write(str(i)+ '\n' + ',') #file ekak write karaddi integer pass karanna ba. e nisa string walata convert karanawa.
    

file.close()
'''

#append
file = open("26data.txt",'a')
x = [str(i*2) for i in range(0,100)]
msg = '\n'.join(x)


file.write(msg)

file.close()



