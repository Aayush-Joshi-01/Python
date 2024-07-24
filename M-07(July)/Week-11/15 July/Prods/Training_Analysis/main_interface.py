from Routes.analysis_url import route
from Decorators.Logger_Analysis import analysis_logger
from Decorators.Login_Analysis import analysis_login_system

def menu():
    print("\nMenu:")
    print("/grouping for data grouping")
    print("/adv_grouping for advanced grouping operations")
    print("/general_report for generating general reports")
    print("/generate_specific_reports for generating spefic reports")
    print("/generate_growth_reports for growth reports")
    print("/exit, /faux, /out, /no to exit the program")

@analysis_login_system
@analysis_logger
def main():
    while True:
        menu()
        choice = input("Enter your choice with /: ")
        if choice.strip().lower() in ["exit", "out", "no", "faux"]:
            break
        elif choice.strip().lower() == "/generate_specific_reports":
            status = input("Enter status (or leave blank): ")
            score_column = input("Enter score column (or leave blank): ")
            skill = input("Enter skill (or leave blank): ")
            date_column = input("Enter date column (or leave blank): ")
            route(choice.strip().lower(), status=status, score_column=score_column, skill=skill,
                  date_column=date_column)
        route(choice)


if __name__ == "__main__":
    main()
