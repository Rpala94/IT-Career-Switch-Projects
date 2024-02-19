#Displaying Working Directory

import os

dirpath = os.getcwd()
print("Your current directory is: " + dirpath)

foldername = os.path.basename(dirpath)

print("The directory name is: " + foldername)
