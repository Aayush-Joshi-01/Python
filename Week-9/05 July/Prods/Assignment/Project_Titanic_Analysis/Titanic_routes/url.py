from typing import Any, Callable, Dict
from ..Titanic_Controllers.route_controllers import C_Survival, C_Demographic, C_Financial, C_Class, C_Additonal


urlpatterns: Dict[str, Callable[..., Any]] = {
    "/survival" : C_Survival.route,
    "/demographic" : C_Demographic.route,
    "/finance" : C_Financial.route,
    "/class" : C_Class.route,
    "/additonal" : C_Additonal.route,

    "/survival/overall" : C_Survival.overall_survival_rate,
    "/survival/class" : C_Survival.survival_by_class,
    "/survival/gender" : C_Survival.survival_by_gender,
    "/survival/age" : C_Survival.survival_by_age_group,
    "/survival/f_size" : C_Survival.survival_by_family_size,

    "/demographic/p_count_by_cls" : C_Demographic.passenger_count_by_class,
    "/demographic/gen_dist" : C_Demographic.gender_distribution,
    "/demographic/age_dist" : C_Demographic.age_distribution,
    "/demographic/embark" : C_Demographic.embarkation_port_analysis,

    "/finance/ticket_fare_dist" : C_Financial.ticket_fare_distribution,
    "/finance/avg_fare" : C_Financial.average_fare_by_class,
    "/finance/fare_vs_survival" : C_Financial.fare_vs_survival,

    "/class/pass_demo_by_cls" : C_Class.pass_demo_by_cls,
    "/class/survival_by_cls" : C_Class.survival_by_cls,
    "/class/fare_by_cls" : C_Class.fare_by_cls,
    
    "/additonal/fam_rel_survival" : C_Additonal.family_relationships_and_survival
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
            return view(url, *args, **kwargs)
        raise Exception("404 Not Found\n")
    except Exception as e:
        print(e)
