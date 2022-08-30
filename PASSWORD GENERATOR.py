import string
import random
import time
print("HELLO")
time.sleep(1)
print("LOADING PASSWORD GENERATOR...")
time.sleep(2)
s1 = string.ascii_uppercase
s2 = string.digits
s3 = string.punctuation
s4 = string.ascii_lowercase


length =int(input("LENGTH OF THE PASSWORD....?\n"))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
s.extend(list(s5))

random.shuffle(s)
print("".join(s[0:length] ))
