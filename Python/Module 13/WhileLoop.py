#Working with While Loops
print("While Loops")
print("--------------------------------------")


a = 1
while a< 6:
    print(a)
    a+=1

print("End of the loop")

print("--------------------------------------")


x = "Hello World"
y = 1
while y <= 3:
    print(x)
    y += 1

print("End of the 2nd loop")

print("--------------------------------------")


print("While Loop with Continue")
x = 0
while x < 6:
    x +=1
    if x == 4:
        continue
    print(x)

print("--------------------------------------")


print("While Loop with Continue")
x = 0
while x < 6:
    x +=1
    if x != 4:
        continue
    print(x)

print("\n")
print("--------------------------------------")

print("While Loop with Break")
a = 1
while a < 14:
    print(a)
    if a == 4:
        print("It's equal to 4, time to stop")
        break
    a += 1

print("--------------------------------------")
#Examples
a = 1
while a<= 3:
    print("Great Job")
    a += 1



x = 1
while x < 10:
    print(x)
    if x == 6:
        print("Break Point")
        break
    x += 1
print("--------------------------------------")
