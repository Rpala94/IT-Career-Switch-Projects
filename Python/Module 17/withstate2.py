#With Practice

with open("Hello.txt","w") as file: 
  file.write("Hey There!")

x = open ("Hello.txt","r")
print(x.read())
x.close()
