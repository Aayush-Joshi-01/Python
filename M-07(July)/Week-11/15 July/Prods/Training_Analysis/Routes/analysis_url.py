from typing import Any, Callable, Dict, Optional
from Controller.analysis_controller import AnalysisController
from Decorators.Logger_Analysis import logger_analysis

urlpatterns: Dict[str, Callable[..., Any]] = {
    '/descriptive': AnalysisController().perform_descriptive_analysis,
    '/temporal': AnalysisController().perform_temporal_analysis,
    '/comparative': AnalysisController().perform_comparative_analysis,
    '/spatial': AnalysisController().perform_spatial_analysis,
    '/behavior': AnalysisController().perform_behavioral_analysis,
    '/health': AnalysisController().perform_health_metrics_analysis,
    '/predictive': AnalysisController().perform_predictive_analysis,
}


@logger_analysis
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
