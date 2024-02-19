#Nesting Loops
print("Nesting Loops Examples")
numbers = [1,2,3]
letters = ['a','b','c']

for x in numbers:
    print(x)
    for y in letters:
        print(y)
    print("\n")


print("-----------------------------------")



orders = ['Order 1','Order 2','Order 3']
foods = ['Apple','Banana','Cake','Bread','Jam']

for x in orders:
    print(x)
    for y in foods:
        print(y)
    print("\n")


print("-----------------------------------")

leads = ['Mark','Bob','Sara']
departments =['IT','Public Relations','Human Resources','Sales','Administration']

for x in leads:
    print(x)
    for y in departments:
        print(y)
    print("\n")

print("-----------------------------------")
