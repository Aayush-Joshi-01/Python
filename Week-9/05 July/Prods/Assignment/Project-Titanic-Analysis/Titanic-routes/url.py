from typing import Any, Callable, Dict
from ..Titanic-Controller.route_controllers import C_Survival


urlpatterns: Dict[str, Callable[..., Any]] = {
    "/survival" : C_Survival.routes,
    "/demographic" : C_Demographic.routes,
    "/finance" : C_Financial.routes,
    "/class" : C_Class.routes,
    "/additonal" : C_Additonal.routes,
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
        view: Callable[..., Any] = urlpatterns.get(url)
        if view:
            return view(*args, **kwargs)
        raise Exception("404 Not Found\n")
    except Exception as e:
        print(e)
