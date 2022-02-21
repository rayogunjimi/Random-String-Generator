
import random
import string


lowercase = True
uppercase = True
numeric = True
symbol = True

repeat = True

size = 10

random.seed()

randomset = ""
if lowercase:
    randomset += string.ascii_lowercase
if uppercase:
    randomset += string.ascii_uppercase
if numeric:
    randomset += string.digits
if symbol:
    randomset += string.punctuation

if repeat:
    print ( ''.join(random.choice(randomset) for i in range(size)) )
else:
    print ( ''.join(random.sample(randomset) for i in range(size)) )