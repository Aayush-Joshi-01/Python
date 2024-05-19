# get name
# get usermail
# get password and if the password contains name or usermail give error
# name should be greater than 3 characters
# the password shoudld check all the permutations
# usermail should start with the name
def get_name():
    name = input("Enter your name: ")
    if len(name) >= 3:
        return name
    else:
        print("Your name should be greater than 3 characters")
        get_name()

def get_usermail(name):
    usermail = input("Enter your usermail: ")
    if name in usermail[:len(name)]:
        return usermail, name
    else:
        print("Your usermail should start with your name")
        get_usermail(name)

def get_password(func):
    usermail, name = func
    password = input("Enter your password: ")
    if name not in password and usermail not in password:
        return password
    else:
        print("Your password should not contain your name or usermail")
        get_password(func)

def signup():
    get_password(get_usermail(get_name()))


if __name__ == '__main__':
    signup()
