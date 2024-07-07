from typing import Any, Callable, Dict
from ..Titanic_routes.url import route


class C_Survival:

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
        pass

    def survival_by_class(self):
        print("Survival by Class")

    def survival_by_gender(self):
        print("Survival by Gender")

    def survival_by_age_group(self):
        print("Survival by Age Group")

    def survival_by_family_size(self):
        print("Survival by Family Size")


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
        print("Passenger Count by Class")

    def gender_distribution(self):
        print("Gender Distribution")

    def age_distribution(self):
        print("Age Distribution")

    def embarkation_port_analysis(self):
        print("Embarkation Port Analysis")


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
        print("Ticket Fare Distribution")

    def average_fare_by_class(self):
        print("Average Fare by Class")

    def fare_vs_survival(self):
        print("Fare vs Survival")


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
        print("Passenger Demographics by Class")

    def survival_by_cls(self):
        print("Survival Rate by Class")

    def fare_by_cls(self):
        print("Fare Analysis by Class")


class C_Additonal:
    def route(self, url: str):
        print("\nAdditional Analysis:")
        print("/fam_rel_survival for family relationships and survival")
        sub_choice = input("\nEnter your choice url with /: ")
        url = url + sub_choice
        route(url)

    def family_relationships_and_survival(self):
        print("Family Relationships and Survival")
