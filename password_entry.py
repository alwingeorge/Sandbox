# Alwin George
min_length = 4

password = input(("Enter password of at least {} characters: ".format(min_length)))
while len(password) < min_length:
    password = input("Enter password of at least {} characters: ".format(min_length))

print('*' * len(password))