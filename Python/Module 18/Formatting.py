#Formatting Output

salary = 44000
txt = "You make £{} pounds a year"
print(txt.format(salary))


print("---------------------------------------------")

print("Multiple Curly Brackets")

string = "Dave teaches {} {}. "
print(string.format("cyber", "secruity"))


print("---------------------------------------------")

string = "Dave loves {} {} and has {} {}. "
print(string.format("cyber", "secruity", 14, "certifications"))

print("---------------------------------------------")

string = "Dave loves {1} {3} and has {2} {0}. "
print(string.format("kids","cyber",7, "secruity"))

print("---------------------------------------------")

string = "Bob likes to play {act} and eat {1}{0}."
print(string.format("dogs","hot", act="games"))

print("---------------------------------------------")

print("Bob likes to play {act} and eat {1}{0}.".format("dogs", "hot",act="games"))
