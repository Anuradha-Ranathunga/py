f = open("demofile.txt", "w")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open("myfile.txt" , "x")