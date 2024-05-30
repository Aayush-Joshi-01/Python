from typing import Callable, List, Tuple

from bank import Bank

urlpatterns: List[Tuple[str, Callable]] = [
    ("create_account", Bank.create_account),
    ("deposit", Bank.deposit),
    ("credit", Bank.credit),
    ("statement", Bank.statement),
    ("transfer", Bank.transfer),
    ("view_transactions", Bank.view_transactions),
]


def route(url: str, *args, **kwargs) -> None:
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
    for pattern, view in urlpatterns:
        if url == pattern:
            return view(*args, **kwargs)
    raise Exception("404 Not Found")
