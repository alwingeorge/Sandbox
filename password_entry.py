# Alwin George
min_length = 4

password = input(("Enter password of at least {} characters: ".format(min_length)))


def get_password():
    global password
    while len(password) < min_length:
        password = input("Enter password of at least {} characters: ".format(min_length))


get_password()

print('*' * len(password))