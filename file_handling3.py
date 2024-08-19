filePath="myfile.txt"

with open(file=filePath, mode="w") as file:
    file.write("fuck me")
    print("inside with block")
    
print("outside with block")