class AccountError(Exception):
    pass

class AccountNotFoundError(AccountError):
    pass

class InsufficientFundsError(AccountError):
    pass

class AccountAlreadyExistsError(AccountError):
    pass

class InvalidInitialBalanceError(AccountError):
    pass
