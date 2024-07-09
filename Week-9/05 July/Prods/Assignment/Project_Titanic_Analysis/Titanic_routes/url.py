from typing import Any, Callable, Dict, Optional
from Titanic_Controllers.route_controllers import C_Survival, C_Demographic, C_Financial, C_Class, C_Additional

# Dictionary mapping URLs to controller methods
urlpatterns: Dict[str, Callable[..., Any]] = {
    "/survival": C_Survival.routes,
    "/demographic": C_Demographic.routes,
    "/finance": C_Financial.routes,
    "/class": C_Class.routes,
    "/additional": C_Additional.routes,
}

def route(url: str, *args: Any, **kwargs: Any) -> Any:
    """
    Routes a URL to a view function.

    Args:
        url (str): The URL to route.
        *args: Variable length arguments to pass to the view function.
        **kwargs: Variable keyword arguments to pass to the view function.

    Raises:
        Exception: If the URL is not found.

    Returns:
        Any: The result of the view function.
    """
    try:
        view: Optional[Callable[..., Any]] = urlpatterns.get(url)
        if view:
            return view(url, *args, **kwargs)
        raise Exception("404 Not Found\n")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # Example usage:
    choice: str = input("Enter the URL for analysis (e.g., /survival): ")
    route(choice)
