from Routes.analysis_urls import route


def menu():
    print("\nMenu:")
    print("1. Perform Basic Grouping")
    print("2. Perform Advanced Grouping")
    print("3. Generate General Reports")
    print("4. Generate Specific Reports")
    print("5. Generate Growth Reports")
    print("6. Exit")


def main():
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")
        if choice.strip().lower() in ["exit", "out", "no", "faux"]:
            break
        elif choice.strip().lower() == "generate_specific_reports":
            status = input("Enter status (or leave blank): ")
            score_column = input("Enter score column (or leave blank): ")
            skill = input("Enter skill (or leave blank): ")
            date_column = input("Enter date column (or leave blank): ")
            route(choice.strip().lower(), status=status, score_column=score_column, skill=skill,
                  date_column=date_column)
        route(choice)


if __name__ == "__main__":
    main()
