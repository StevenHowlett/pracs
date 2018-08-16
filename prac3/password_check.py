"""Steven Howlett"""
MIN_LENGTH=3
def main():
    password = get_password()
    print('*'*len(password))


def get_password():
    password = input("password:")
    while len(password) < MIN_LENGTH:
        password = input("enter password with a min of 3 characters")
    return password


main()