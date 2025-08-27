import random

numchars=20
password=""

for i in range(numchars):
    charcode=random.randrange(0,25) + ord('a')
    password+=chr(charcode)

print(password)
