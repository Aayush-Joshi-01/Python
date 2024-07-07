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
        df = data_structuring()
        self.df = df
        

    @staticmethod
    def routes(url: str):
        print("\nSurvival Analysis:")
        print("/overall for overall analysis")
        print("/class for class analysis")
        print("/gender for gender analysis")
        print("/age for age analysis")
        print("/f_size for family size analyis")
        sub_choice = input("\nEnter your choice url with /: ")
        url = url + sub_choice
        route(url)

    def overall_survival_rate(self):
        print(Survival_Controller().overall_survival_rate(self.df))

    def survival_by_class(self):
        print(Survival_Controller().survival_by_class(self.df))

    def survival_by_gender(self):
        print(Survival_Controller().survival_by_gender(self.df))

    def survival_by_age_group(self):
        print(Survival_Controller().survival_by_age_group(self.df))

    def survival_by_family_size(self):
        print(Survival_Controller().survival_by_family_size(self.df))


class C_Demographic:
    def routes(self, url: str):
        print("\nDemographic Analysis:")
        print("/p_count_by_cls for passenger count by class")
        print("/gen_dist for gender distribution")
        print("/age_dist for age distribution")
        print("/embark for embarkation port analysis")
        sub_choice = input("\nEnter your choice url with /: ")
        url = url + sub_choice
        route(url)

    def passenger_count_by_class(self):
        print(Demographic_Controller().passenger_count_by_class(self.df))

    def gender_distribution(self):
        print(Demographic_Controller().gender_distribution(self.df))

    def age_distribution(self):
        Demographic_Controller().age_distribution(self.df)

    def embarkation_port_analysis(self):
        print(Demographic_Controller().embarkation_port_analysis(self.df))


class C_Financial:
    def routes(self, url: str):
        print("\nFinancial Analysis:")
        print("/ticket_fare_dist for ticket fare distribution")
        print("/avg_fare for average fare")
        print("/fare_vs_survival for fare vs survival")
        sub_choice = input("\nEnter your choice url with /: ")
        url = url + sub_choice
        route(url)

    def ticket_fare_distribution(self):
        Financial_Controller().ticket_fare_distribution(self.df)

    def average_fare_by_class(self):
        print(Financial_Controller().average_fare_by_class(self.df))

    def fare_vs_survival(self):
        Financial_Controller().fare_vs_survival(self.df)


class C_Class:
    def route(self, url: str):
        print("\nClass Analysis:")
        print("/pass_demo_by_cls for passenger demographics by class")
        print("/survival_by_cls for survival rate by class")
        print("/fare_by_cls for fare analysis by class")
        sub_choice = input("\nEnter your choice url with /: ")
        url = url + sub_choice
        route(url)

    def pass_demo_by_cls(self):
        print(Class_Controller().passenger_demographics_by_class(self.df))

    def survival_by_cls(self):
        print(Class_Controller().survival_rates_by_class_and_gender(self.df))

    def fare_by_cls(self):
        Class_Controller().fare_analysis_by_class(self.df)


class C_Additonal:
    def route(self, url: str):
        print("\nAdditional Analysis:")
        print("/fam_rel_survival for family relationships and survival")
        sub_choice = input("\nEnter your choice url with /: ")
        url = url + sub_choice
        route(url)

    def family_relationships_and_survival(self):
        print(Additonal_Controller().family_relationships_and_survival(self.df))
    
    # def survival_rate_by_category(self):
    #     print(Additonal_Controller().custom_class_survival(self.df))

    
