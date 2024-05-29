urlpatterns = [
    ("deposit", "bank/deposit"),
    ("withdraw", "bank/withdraw"),
    ("transfer", "bank/transfer"),
    ("balance", "bank/balance"),
    ("add_account", "bank/add_account"),
]


def route(url, *args, **kwargs):
    for pattern, view in urlpatterns:
        if pattern == url:
            module_name, func_name = view.split("/")
            module = globals()[module_name]
            func = getattr(module, func_name)
            return func(*args, **kwargs)
        raise Exception("404 Not Found!")
