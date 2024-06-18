from typing import Any, Callable, Dict
from ..controllers.bank_controller import BankController
from ..decorators.generate_logs import logger_v

urlpatterns: Dict[str, Callable[..., Any]] = {
    "create_account": BankController.create_account,
    "get_account_details": BankController.get_account_details,
    "deposit": BankController.deposit,
    "debit": BankController.debit,
    "credit": BankController.credit,
    "transfer": BankController.transfer,
    "view_transactions": BankController.view_transactions,
}


@logger_v
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
