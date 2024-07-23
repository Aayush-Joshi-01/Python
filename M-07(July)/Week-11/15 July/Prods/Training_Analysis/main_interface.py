def menu():
    print("\nMenu:")
    print("1. Perform Basic Grouping")
    print("2. Perform Advanced Grouping")
    print("3. Generate General Reports")
    print("4. Generate Specific Reports")
    print("5. Generate Growth Reports")
    print("6. Exit")

def main():
    df = DataLoader().load_data()  # Load your DataFrame
    controller = DataProcessorController(df)

    while True:
        menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            controller.perform_basic_grouping()
        elif choice == '2':
            controller.perform_advanced_grouping()
        elif choice == '3':
            controller.generate_general_reports()
        elif choice == '4':
            status = input("Enter status (or leave blank): ")
            score_column = input("Enter score column (or leave blank): ")
            skill = input("Enter skill (or leave blank): ")
            date_column = input("Enter date column (or leave blank): ")
            controller.generate_specific_reports(status=status, score_column=score_column, skill=skill, date_column=date_column)
        elif choice == '5':
            controller.generate_growth_reports()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()