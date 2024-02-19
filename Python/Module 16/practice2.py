#Practice Answer 2
import shutil
import os
x = open("MyNewFile.txt","x")
x.close()

x = open("MyNewFile.txt","a")
x.write("Here is line 1 \n")
x.write("Here is line 2 \n")
x.close()

src = "MyNewFile.txt"
dst = "Beta.txt"

shutil.copy(src,dst)

x = open("Beta.txt", "a")
b = 1

while b < 4:
    x.write("Time for new line" + str(b) + "\n")
    b += 1
x.close()

first = open("Beta.txt", "r")
print(first.read())
first.close()

second = open ("Beta.txt", "r")
print(second.read())
second.close()
    
