#With Statement

x = open("Hello.txt", "w")
y = x.read()
print(y)
x.close()

with open("Hello.txt", "w") as file:
    file.write("Hey There!")
    
