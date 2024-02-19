x = open("ClassFile.txt","x")
x.close()

x = open("ClassFile.txt", "a")
b = 1
while b < 4:
    x.write("Here is line" + str(b) + '\n')
    b += 1
x.close()

x = open ("ClassFile.txt", "r")
print(x.read())
x.close()
