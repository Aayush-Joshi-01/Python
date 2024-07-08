from typing import Any, Callable, Dict
from ..Titanic_routes.url import route
from ..Titanic_Analysis.load_data import data_structuring
from ..Titanic_Controllers.survival_controller import Survival_Controller
from ..Titanic_Controllers.demographic_controller import Demographic_Controller
from ..Titanic_Controllers.financial_controller import Financial_Controller
from ..Titanic_Controllers.class_controller import Class_Controller
from ..Titanic_Controllers.additonal_controller import Additonal_Controller


class C_Survival:
    def __init__(self):
        self.arr: Any = data_structuring()

    @staticmethod
    def routes(url: str) -> None:
        print("\nSurvival Analysis:")
        print("/overall for overall analysis")
        print("/class for class analysis")
        print("/gender for gender analysis")
        print("/age for age analysis")
        print("/f_size for family size analyis")
        sub_choice: str = input("\nEnter your choice url with /: ")
        url: str = url + sub_choice
        route(url)

    def overall_survival_rate(self) -> None:
        print(Survival_Controller().overall_survival_rate(self.arr))

    def survival_by_class(self) -> None:
        print(Survival_Controller().survival_by_class(self.arr))

    def survival_by_gender(self) -> None:
        print(Survival_Controller().survival_by_gender(self.arr))

    def survival_by_age_group(self) -> None:
        print(Survival_Controller().survival_by_age_group(self.arr))

    def survival_by_family_size(self) -> None:
        print(Survival_Controller().survival_by_family_size(self.arr))


class C_Demographic:
    def routes(self, url: str) -> None:
        print("\nDemographic Analysis:")
        print("/p_count_by_cls for passenger count by class")
        print("/gen_dist for gender distribution")
        print("/age_dist for age distribution")
        print("/embark for embarkation port analysis")
        sub_choice: str = input("\nEnter your choice url with /: ")
        url: str = url + sub_choice
        route(url)

    def passenger_count_by_class(self) -> None:
        print(Demographic_Controller().passenger_count_by_class(self.arr))

    def gender_distribution(self) -> None:
        print(Demographic_Controller().gender_distribution(self.arr))

    def age_distribution(self) -> None:
        Demographic_Controller().age_distribution(self.arr)

    def embarkation_port_analysis(self) -> None:
        print(Demographic_Controller().embarkation_port_analysis(self.arr))


class C_Financial:
    def routes(self, url: str) -> None:
        print("\nFinancial Analysis:")
        print("/ticket_fare_dist for ticket fare distribution")
        print("/avg_fare for average fare")
        print("/fare_vs_survival for fare vs survival")
        sub_choice: str = input("\nEnter your choice url with /: ")
        url: str = url + sub_choice
        route(url)

    def ticket_fare_distribution(self) -> None:
        Financial_Controller().ticket_fare_distribution(self.arr)

    def average_fare_by_class(self) -> None:
        print(Financial_Controller().average_fare_by_class(self.arr))

    def fare_vs_survival(self) -> None:
        Financial_Controller().fare_vs_survival(self.arr)


class C_Class:
    def route(self, url: str) -> None:
        print("\nClass Analysis:")
        print("/pass_demo_by_cls for passenger demographics by class")
        print("/survival_by_cls for survival rate by class")
        print("/fare_by_cls for fare analysis by class")
        sub_choice: str = input("\nEnter your choice url with /: ")
        url: str = url + sub_choice
        route(url)

    def pass_demo_by_cls(self) -> None:
        print(Class_Controller().passenger_demographics_by_class(self.arr))

    def survival_by_cls(self) -> None:
        print(Class_Controller().survival_rates_by_class_and_gender(self.arr))

    def fare_by_cls(self) -> None:
        Class_Controller().fare_analysis_by_class(self.arr)


class C_Additonal:
    def route(self, url: str) -> None:
        print("\nAdditional Analysis:")
        print("/fam_rel_survival for family relationships and survival")
        sub_choice: str = input("\nEnter your choice url with /: ")
        url: str = url + sub_choice
        route(url)

    def family_relationships_and_survival(self) -> None:
        print(Additonal_Controller().family_relationships_and_survival(self.arr))

    def survival_rate_by_category(self) -> None:
        category = input("Enter the category (case sensitive): ")
        print(Additonal_Controller().survival_rate_by_category(self.arr, category))
