#Reading Files
print("Reading Files")
print("--------------------------------------------")

a = open("demo.txt","r")
print(a.read())

print("--------------------------------------------")

print("Reading Files - Readline()")

a = open ("demo.txt","r")
print(a.readline())
a.close()
print("--------------------------------------------")

a = open ("demo.txt","r")
print(a.read(7))
a.close()
print("--------------------------------------------")

print("Reading Files -'With'")
with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)
    
print("--------------------------------------------")
print("Writing on Files")
a = open("demo.txt", "a")
a.write("\n Here is another line in our text file")
a.close()

print("--------------------------------------------")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)
    
print("--------------------------------------------")

