employees=['Sara','Tammy','Debbie','John','Carrie']
print(employees)
employees[0] = 'Mark'
print(employees)

employees = employees +['Jim']
print(employees)


fav_nums = ['16','24','7','100']
fav_colors =['Blue','Red','Green','Pink']
print(fav_nums + fav_colors)

employees=['Sara','Tammy','Debbie','John','Carrie']
employees.insert(1,"Dave")
print(employees)

del employees[4]
print(employees)

employees.remove('Carrie')
print(employees)


employees=['Sara','Tammy','Debbie','John','Carrie']
for x in employees:
    print(x)
    

employees=['Sara','Tammy','Debbie','John','Carrie']
if "Tammy" in employees:
    print("Yes, Tammy does work here")
    
    
nums = ['1','2','3','4','5']
print(nums)

nums[3]='10'
print(nums)

print("--------------------------------------------------")

nums = ['1','2','3','4','5']
print(nums)
del nums[2]
print(nums)


print("--------------------------------------------------")


nums =['1','2','3','4']
print(nums)

nums.insert(2,'25')
print(nums)