import random
import sys

numchars=10
if len(sys.argv)>1:
    number_chars=int(sys.argv[1])
password=""

for i in range(numchars):
    character_index=random.randint(0,52)
    character_index+=ord('b')
    password+=chr(char_index)

print(password)
