from bank import Bank
from transaction import Transaction
from typing import Callable, List, Tuple

urlpatterns: List[Tuple[str, Callable]] = [
    ("create_account", Bank.create_account),
    ("deposit", Bank.deposit),
    ("credit", Bank.credit),
    ("statement", Bank.statement),
    ("transfer", Bank.transfer),
    ("view_transactions", Transaction.view_transactions),
]


def route(url: str, *args: object, **kwargs: object) -> None:
    for pattern, view in urlpatterns:
        if url == pattern:
            return view(*args, **kwargs)
    raise Exception("404 Not Found")
