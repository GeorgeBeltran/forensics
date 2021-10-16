import sys
import hashlib
print("Please enter your full name")
line = sys.stdin.readline()
line = line.rstrip()
md5_object = hashlib.md5()
print(md5_object.hexdigest())   # Prints the output as per the hashing algorithm i.e. md5