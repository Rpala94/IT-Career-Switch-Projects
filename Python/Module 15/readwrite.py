#Reading Files
print("----------------------------------------")

with open("demo.txt") as myfile:
    contents =myfile.read()
    print(contents)

a= open("demo.txt", "w")
a.write("What had happened now?")
a.close()

print("----------------------------------------")

with open("demo.txt") as myfile:
    contents =myfile.read()
    print(contents)



y = open("NewFile.txt","x")
