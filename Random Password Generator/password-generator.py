import random as r
import string as s

#1
'''
chars = []
for char in s.printable:
    chars.append(char)

password = ""
i = 0
for i in range(13):
    password += r.choice(chars)
    i+=1
'''
#2
'''
chars = s.ascii_letters+s.digits+s.punctuation
def generate_password(length):
    password = ""
    for i in range(length):
        password += r.choice(chars)
    return password
'''

#3
chars = s.ascii_letters+s.digits+s.punctuation
def genarate_password(length):
    return ''.join(r.choice(chars) for _ in range(length))