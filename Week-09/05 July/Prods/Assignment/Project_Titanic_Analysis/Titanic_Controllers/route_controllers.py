from typing import Any, Callable, Dict, Optional
from Titanic_Analysis.load_data import data_structuring
from Titanic_Controllers.survival_controller import Survival_Controller
from Titanic_Controllers.demographic_controller import Demographic_Controller
from Titanic_Controllers.financial_controller import Financial_Controller
from Titanic_Controllers.class_controller import Class_Controller
from Titanic_Controllers.additional_controller import Additional_Controller

# URL patterns dictionary mapping URLs to controller methods
urlpatterns_controller: Dict[str, Callable[..., Any]] = {

    # Survival Routes
    "/survival/overall": Survival_Controller().overall_survival_rate,
    "/survival/class": Survival_Controller().survival_by_class,
    "/survival/gender": Survival_Controller().survival_by_gender,
    "/survival/age": Survival_Controller().survival_by_age_group,
    "/survival/f_size": Survival_Controller().survival_by_family_size,

    # Demographic Routes
    "/demographic/p_count_by_cls": Demographic_Controller().passenger_count_by_class,
    "/demographic/gen_dist": Demographic_Controller().gender_distribution,
    "/demographic/age_dist": Demographic_Controller().age_distribution,
    "/demographic/embark": Demographic_Controller().embarkation_port_analysis,

    # Financial Routes
    "/finance/ticket_fare_dist": Financial_Controller().ticket_fare_distribution,
    "/finance/avg_fare": Financial_Controller().average_fare_by_class,
    "/finance/fare_vs_survival": Financial_Controller().fare_vs_survival,

    # Class Routes
    "/class/pass_demo_by_cls": Class_Controller().passenger_demographics_by_class,
    "/class/survival_by_cls": Class_Controller().survival_rates_by_class_and_gender,
    "/class/fare_by_cls": Class_Controller().fare_analysis_by_class,

    # Additional Routes
    "/additional/fam_rel_survival": Additional_Controller().family_relationships_and_survival,
    "/additional/survival_rate_by_category": Additional_Controller().survival_rate_by_category,
}


class C_Survival:
    """
    Controller for handling survival-related analyses.
    """

    def __init__(self):
        self.arr: Any = data_structuring()

    @staticmethod
    def routes(url: str) -> None:
        """Interactive method to display available survival analyses."""
        print("\nSurvival Analysis:")
        print("/overall for overall survival rate analysis")
        print("/class for survival rate by class analysis")
        print("/gender for survival rate by gender analysis")
        print("/age for survival rate by age group analysis")
        print("/f_size for survival rate by family size analysis")
        sub_choice: str = input("\nEnter your choice url with /: ")
        route_url: str = url + sub_choice
        controller_route(route_url)

    def overall_survival_rate(self, url: str) -> None:
        """Print overall survival rate."""
        print(Survival_Controller().overall_survival_rate(self.arr))

    def survival_by_class(self, url: str) -> None:
        """Print survival rates by passenger class."""
        print(Survival_Controller().survival_by_class(self.arr))

    def survival_by_gender(self, url: str) -> None:
        """Print survival rates by gender."""
        print(Survival_Controller().survival_by_gender(self.arr))

    def survival_by_age_group(self, url: str) -> None:
        """Print survival rates by age group."""
        print(Survival_Controller().survival_by_age_group(self.arr))

    def survival_by_family_size(self, url: str) -> None:
        """Print survival rates by family size."""
        print(Survival_Controller().survival_by_family_size(self.arr))


class C_Demographic:
    """
    Controller for handling demographic-related analyses.
    """

    def __init__(self):
        self.arr: Any = data_structuring()

    @staticmethod
    def routes(url: str) -> None:
        """Interactive method to display available demographic analyses."""
        print("\nDemographic Analysis:")
        print("/p_count_by_cls for passenger count by class analysis")
        print("/gen_dist for gender distribution analysis")
        print("/age_dist for age distribution analysis")
        print("/embark for embarkation port analysis")
        sub_choice: str = input("\nEnter your choice url with /: ")
        route_url: str = url + sub_choice
        controller_route(route_url)

    def passenger_count_by_class(self, url: str) -> None:
        """Print passenger count by class."""
        print(Demographic_Controller().passenger_count_by_class(self.arr))

    def gender_distribution(self, url: str) -> None:
        """Print gender distribution."""
        print(Demographic_Controller().gender_distribution(self.arr))

    def age_distribution(self, url: str) -> None:
        """Display age distribution plot."""
        Demographic_Controller().age_distribution(self.arr)

    def embarkation_port_analysis(self, url: str) -> None:
        """Print embarkation port analysis."""
        print(Demographic_Controller().embarkation_port_analysis(self.arr))


class C_Financial:
    """
    Controller for handling financial-related analyses.
    """

    def __init__(self):
        self.arr: Any = data_structuring()

    @staticmethod
    def routes(url: str) -> None:
        """Interactive method to display available financial analyses."""
        print("\nFinancial Analysis:")
        print("/ticket_fare_dist for ticket fare distribution analysis")
        print("/avg_fare for average fare analysis")
        print("/fare_vs_survival for fare vs survival analysis")
        sub_choice: str = input("\nEnter your choice url with /: ")
        route_url: str = url + sub_choice
        controller_route(route_url)

    def ticket_fare_distribution(self, url: str) -> None:
        """Display ticket fare distribution plot."""
        Financial_Controller().ticket_fare_distribution(self.arr)

    def average_fare_by_class(self, url: str) -> None:
        """Print average fare by class."""
        print(Financial_Controller().average_fare_by_class(self.arr))

    def fare_vs_survival(self, url: str) -> None:
        """Display fare vs survival plot."""
        Financial_Controller().fare_vs_survival(self.arr)


class C_Class:
    """
    Controller for handling class-related analyses.
    """

    def __init__(self):
        self.arr: Any = data_structuring()

    @staticmethod
    def routes(url: str) -> None:
        """Interactive method to display available class-related analyses."""
        print("\nClass Analysis:")
        print("/pass_demo_by_cls for passenger demographics by class analysis")
        print("/survival_by_cls for survival rate by class analysis")
        print("/fare_by_cls for fare analysis by class analysis")
        sub_choice: str = input("\nEnter your choice url with /: ")
        route_url: str = url + sub_choice
        controller_route(route_url)

    def pass_demo_by_cls(self, url: str) -> None:
        """Print passenger demographics by class."""
        print(Class_Controller().passenger_demographics_by_class(self.arr))

    def survival_by_cls(self, url: str) -> None:
        """Print survival rates by class and gender."""
        print(Class_Controller().survival_rates_by_class_and_gender(self.arr))

    def fare_by_cls(self, url: str) -> None:
        """Print fare analysis by class."""
        Class_Controller().fare_analysis_by_class(self.arr)


class C_Additional:
    """
    Controller for handling additional analyses.

    Attributes:
        arr (Any): Processed Titanic dataset.

    Methods:
        routes(url: str) -> None:
            Interactive method to display available additional analyses.
        family_relationships_and_survival(url: str) -> None:
            Print family relationships and survival analysis.
        survival_rate_by_category(url: str) -> None:
            Print survival rate by specified category.
    """

    def __init__(self):
        self.arr: Any = data_structuring()

    @staticmethod
    def routes(url: str) -> None:
        """Interactive method to display available additional analyses."""
        print("\nAdditional Analysis:")
        print("/fam_rel_survival for family relationships and survival analysis")
        print("/survival_rate_by_category for survival rate by category analysis")
        sub_choice: str = input("\nEnter your choice url with /: ")
        route_url: str = url + sub_choice
        controller_route(route_url)

    def family_relationships_and_survival(self, url: str) -> None:
        """Print family relationships and survival analysis."""
        print(Additional_Controller().family_relationships_and_survival(self.arr))

    def survival_rate_by_category(self, url: str) -> None:
        """Print survival rate by specified category."""
        category = input("Enter the category (case sensitive): ")
        print(Additional_Controller().survival_rate_by_category(self.arr, category))


def controller_route(url: str, *args: Any, **kwargs: Any) -> Any:
    """
    Routes a URL to a view function.
    """
    try:
        view: Optional[Callable[..., Any]] = urlpatterns_controller.get(url)
        if view:
            return view(url, *args, **kwargs)
        raise Exception("404 Not Found\n")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    choice: str = input("Enter the URL for analysis: ")
    controller_route(choice)
