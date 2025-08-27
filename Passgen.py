import random
import sys

numchars=10
if len(sys.argv)>1:
    numchars=int(sys.argv[1])
password=""

for i in range(numchars):
    ordinal=random.randrange(0,51)
    charcode=ordinal + 65
    password+=chr(charcode)

print(password)
