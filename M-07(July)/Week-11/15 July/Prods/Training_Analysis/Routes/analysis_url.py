from typing import Any, Callable, Dict, Optional
from Controller.analysis_controller import DataProcessorController

urlpatterns: Dict[str, Callable[..., Any]] = {
    "/grouping": DataProcessorController().perfrom_basic_grouping,
    "/adv_grouping": DataProcessorController().perfrom_advanced_grouping,
    "/general_reports": DataProcessorController().generate_general_reports,
    "/generate_specific_reports": DataProcessorController().generate_specific_reports,
    "/generate_growth_reports": DataProcessorController().generate_growth_reports,
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
        view: Optional[Callable[..., Any]] = urlpatterns.get(url)
        if view:
            return view(*args, **kwargs)
        raise Exception("404 Not Found\n")
    except Exception as e:
        print(e)
