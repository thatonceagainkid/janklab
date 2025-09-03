import random
import sys

numchars=10
if len(sys.argv)>1:
    numchars=int(sys.argv[1])
password=""

for i in range(numchars):
    char_index=random.randint(0,52)
    char_index+=ord('b')
    password+=chr(char_index)

print(password)
