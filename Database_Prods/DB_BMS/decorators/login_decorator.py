from typing import Callable, Any
from Database_Prods.DB_BMS.decorators.generate_logs import logger_v


@logger_v
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
            print("You are logged-in")
            return func(*args, **kwargs)
            # returns the wrapped function as logged-in user
        else:
            print("You are not logged-in")
            # returns the wrapped function as not logged-in us

    return wrapper
