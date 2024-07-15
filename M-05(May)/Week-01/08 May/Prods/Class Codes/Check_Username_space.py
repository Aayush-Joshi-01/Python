# check and validate the username even if there is mistaken spaces after the username
USER = 'aayush'


def validate_username(username):
    userlist = username.split(' ')
    if userlist[0] == USER:
        return True
    else:
        return False


def without_validation(username):
    if username == USER:
        return True
    else:
        return False


def check_username():
    username = input('Please enter your username: ')
    print(without_validation(username))
    if validate_username(username):
        return True
    else:
        return False


print(check_username())
