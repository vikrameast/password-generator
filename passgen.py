import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ACDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-;:,./<>?`~'

number = input('Number of passwords? - ')
number = int(number)

length = input('Password length - ')
length = int(length)

for _ in range(number):
    password = ''
    for __ in range(length):
        password += random.choice(chars)
    print(password)
