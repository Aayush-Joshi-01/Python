from typing import Any, Callable, Dict

from controllers.bank_controller import BankController
from controllers.transaction_controller import TransactionController

urlpatterns: Dict[str, Callable[..., Any]] = {
    "create_account": BankController.create_account,
    "get_account_details": BankController.get_account_details,
    "deposit": TransactionController.deposit,
    "debit": TransactionController.debit,
    "credit": TransactionController.credit,
    "transfer": TransactionController.transfer,
    "view_transactions": BankController.view_transactions,
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