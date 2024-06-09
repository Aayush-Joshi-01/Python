from typing import Callable, Any


def login_banking_system(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that checks if the user is logged in before calling the decorated function.

    Args:
        func: The function to decorate.

    Returns: the main function to execute the code
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        username = input("Enter the admin Username: ")
        password = input("Enter the admin Password: ")
        if username == "admin" and password == "123":
            return func(*args, **kwargs)
            # returns the wrapped function as logged-in user
        else:
            print("You are not logged-in")
            # returns the wrapped function as not logged-in us

    return wrapper
