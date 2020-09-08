minimum_length = 4


def main():
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(line):
    """Print pre-determined number of asterisks"""
    print('*' * len(line))


def get_password(minimum_length):
    """Get password and check for length"""
    password = input("Password must have at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Password must have at least {} characters: ".format(minimum_length))
    return password


main()