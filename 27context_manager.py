#file eka open karala close karanna amataka wenawata
with open("26data.txt" , 'a') as file:
    x = [str(i*2) for i in range(0,100)]
    msg = '\n'.join(x)
    file.write(msg)

#with walin aluthin context ekak open wenawa. ema block eka iwara weddi relevant resource eka automatically close wenawa. 
    
   
