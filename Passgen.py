import random
import sys

numchars=10
if len(sys.argv)>1:
    numchars=int(sys.argv[1])
password=""

for i in range(numchars):
    charcode=random.randrange(0,25) + ord('a')
    password+=chr(charcode)

print(password)
