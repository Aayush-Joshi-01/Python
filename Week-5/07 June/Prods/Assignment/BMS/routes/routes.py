from typing import Callable, Tuple, List, Any

urlpatterns: List[Tuple[str, Callable]] = [
    # ("create_account", ),
    # ("debit", ),
    # ("credit", ),
    # ("statement", ),
    # ("transfer", ),
    # ("view_transactions", ),
]


def route(url: str, *args: Any, **kwargs: Any) -> Callable:
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
        for pattern, view in urlpatterns:
            if url == pattern:
                return view(*args, **kwargs)
        raise Exception("404 Not Found\n")
    except Exception as e:
        print(e)
