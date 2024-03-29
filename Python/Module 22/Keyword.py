#Using Keyword and Positional Arguments

def greet(name, msg = " How are you today? "):
    print("Hey",name + "," + msg)

print("2 Keywords")
greet(name = "Dave", msg = " How do you do?")

print("--------------------------------------------------------")

print("2 Keywords, out of order")

greet(msg = " How are you doing?", name = "Dave")

print("--------------------------------------------------------")

print("1 postional, 1 keyword")
greet("Dave", msg = " How you doin?")
print("--------------------------------------------------------")
print("Default argument")
greet("Dave")
