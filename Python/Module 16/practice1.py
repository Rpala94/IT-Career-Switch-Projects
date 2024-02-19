#Practice Answer 1
import shutil
import os

src ="practiceFile.txt"
dst ="NewDemo.txt"

shutil.copy(src,dst)

os.rename("NewDemo.txt","Alpha.txt")

x= open("Alpha.txt","r")
print(x.read())
x.close()
