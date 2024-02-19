x = open("MyNewFile.txt","x")
x.close()

x=open("MyNewFile.txt", "a")
x.write("Here is line 1"'\n')
x.write("Here is line 2" '\n')
x.close()

x=open("MyNewFile.txt","r")
print(x.read())


print("-----------------------------------------------")
print("Answer #2\n")

x = open("ClassFile.txt","x")
x.close()

x = open("ClassFile.txt", "a")
b = 1
while b < 4:
    x.write("Here is line " + str(b) + '\n')
    b += 1
x.close()

x = open ("ClassFile.txt", "r")
print(x.read())
x.close()
