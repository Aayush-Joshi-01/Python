def validate_length(input_str, max_length, field_name):
    if len(input_str) > max_length:
        raise ValueError(f"{field_name} must be {max_length} characters or fewer.")
    return input_str


def get_username():
    while True:
        try:
            username = input("Enter a username (max 20 characters): ")
            validate_length(username, 20, "Username")
            return username
        except ValueError as e:
            print(e)


def get_password():
    while True:
        try:
            password = input("Enter a password (max 50 characters): ")
            validate_length(password, 50, "Password")
            return password
        except ValueError as e:
            print(e)


def get_email():
    while True:
        try:
            email = input("Enter an email (max 50 characters): ")
            validate_length(email, 50, "Email")
            return email
        except ValueError as e:
            print(e)


def main():
    print("Welcome to the sensitive data validation program!")

    username = get_username()
    password = get_password()
    email = get_email()

    print("All inputs are valid.")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")


if __name__ == "__main__":
    main()
