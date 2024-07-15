class AccountError(Exception):
    """
    Base class for all account-related exceptions.
    """
    pass


class AccountNotFoundError(AccountError):
    """
    Raised when an account is not found.

    Attributes:
        message (str): The error message.
    """
    pass


class InsufficientFundsError(AccountError):
    """
    Raised when an account does not have sufficient funds.

    Attributes:
        message (str): The error message.
    """
    pass


class AccountAlreadyExistsError(AccountError):
    """
    Raised when an account with the same account number already exists.

    Attributes:
        message (str): The error message.
    """
    pass


class InvalidInitialBalanceError(AccountError):
    """
    Raised when the initial balance of an account is invalid.

    Attributes:
        message (str): The error message.
    """
    pass
