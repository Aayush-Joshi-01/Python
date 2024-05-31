def login_banking_system(func):
    """
    A decorator that checks if the user is logged in before calling the decorated function.

    Args:
        func: The function to decorate.

    Returns: the main function to execute the code
    """

    def wrapper(*args, **kwargs):
        username = input("Enter the admin Username: ")
        password = input("Enter the admin Password: ")
        if username == "admin" and password == "123":
            return func(*args, **kwargs)

    return wrapper
