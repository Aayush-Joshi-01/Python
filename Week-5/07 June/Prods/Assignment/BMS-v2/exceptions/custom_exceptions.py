class AccountError(Exception):
    """
    Base class for all account-related exceptions.
    """
    def __init__(self, message) -> None:
        self.message = message
        print(self.message)
        super().__init__(message)
    pass


class AccountNotFoundError(AccountError):
    """
    Raised when an account is not found.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class InsufficientFundsError(AccountError):
    """
    Raised when an account does not have sufficient funds.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class AccountAlreadyExistsError(AccountError):
    """
    Raised when an account with the same account number already exists.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class InvalidInitialBalanceError(AccountError):
    """
    Raised when the initial balance of an account is invalid.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
