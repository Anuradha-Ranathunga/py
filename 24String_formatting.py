name = "Anuradha"
height = 176

        #method 1=> String concatenation
message ="Hello " + name + ". Your height is " + str(height) #height, int ekak wana nisa eka string walata convert kara gannawa. 

        #method 2
message = "Hello %s. Your height is %d. "%(name, height) #c type formatting
#%s=> string , %d=> decimal numbers 
# %f=> float , %.2f => dashamasthana 2 kata format karanna
#%05d => 00176
#(name,height)=> meke piliwela wadagath wenawa. 

        #method 3
message = "Hello {}. Your height is {}" .format(name, height) #call the format function. 
#if you want, indexing karannath puluwan
message = "Hello {0}. Your height is {1} ({0})" .format(name, height) #0 weni parameter eka and 2 weni paramter eka meyin adahas wenawa. 
#pros=>interchange walin parameters maru karanna puluwan. e menma dila thiyena parameter eka reuse karanna puluwan. 

#percentage configeration waladi use karapu setting ma mehidida bawitha karanna puluwan.
message = "Hello {}. Your height is {:05d}" .format(name, height)

        #method 4=> f String formatting
message= f"Hello {name}. Your height is {height}"
message= f"Hello {name}. Your height is {height:05d}"
message= f"Hello {len(name)}. Your height is {height:05d}"

print(message)