import random
import os

random_str = ""

for i in range(10000):
	random_str += str(i)+"\n"
	#random_str += chr(random.randint(97, 122))
try:
	os.system("rm random_file.txt")
except:
	pass

os.system("touch random_file.txt")
with open("random_file.txt", "w") as f:
	f.write(random_str)