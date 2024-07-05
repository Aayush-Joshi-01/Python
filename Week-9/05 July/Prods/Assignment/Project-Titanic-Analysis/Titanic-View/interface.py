def main():
    while True:
        print("\nTitanic Dataset Analysis Menu:")
        print("1. Survival Analysis")
        print("2. Demographic Analysis")
        print("3. Financial Analysis")
        print("4. Class Analysis")
        print("5. Additional Insights")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            print("\nSurvival Analysis:")
            print("a. Overall Survival Rate")
            print("b. Survival by Class")
            print("c. Survival by Gender")
            print("d. Survival by Age Group")
            print("e. Survival by Family Size")
            sub_choice = input("\nEnter your choice (a-e): ")
            if sub_choice == 'a':
                print("Overall Survival Rate:", overall_survival_rate(df))
            elif sub_choice == 'b':
                print("Survival by Class:\n", survival_by_class(df))
            elif sub_choice == 'c':
                print("Survival by Gender:\n", survival_by_gender(df))
            elif sub_choice == 'd':
                print("Survival by Age Group:\n", survival_by_age_group(df))
            elif sub_choice == 'e':
                print("Survival by Family Size:\n", survival_by_family_size(df))

        elif choice == '2':
            print("\nDemographic Analysis:")
            print("a. Passenger Count by Class")
            print("b. Gender Distribution")
            print("c. Age Distribution")
            print("d. Embarkation Port Analysis")
            sub_choice = input("\nEnter your choice (a-d): ")
            if sub_choice == 'a':
                print("Passenger Count by Class:\n", passenger_count_by_class(df))
            elif sub_choice == 'b':
                print("Gender Distribution:\n", gender_distribution(df))
            elif sub_choice == 'c':
                age_distribution(df)
            elif sub_choice == 'd':
                print("Embarkation Port Analysis:\n", embarkation_port_analysis(df))

        elif choice == '3':
            print("\nFinancial Analysis:")
            print("a. Ticket Fare Distribution")
            print("b. Average Fare by Class")
            print("c. Fare vs. Survival")
            sub_choice = input("\nEnter your choice (a-c): ")
            if sub_choice == 'a':
                ticket_fare_distribution(df)
            elif sub_choice == 'b':
                print("Average Fare by Class:\n", average_fare_by_class(df))
            elif sub_choice == 'c':
                fare_vs_survival(df)

        elif choice == '4':
            print("\nClass Analysis:")
            print("a. Passenger Demographics by Class")
            print("b. Survival Rates by Class and Gender")
            print("c. Fare Analysis by Class")
            sub_choice = input("\nEnter your choice (a-c): ")
            if sub_choice == 'a':
                print("Passenger Demographics by Class:\n", passenger_demographics_by_class(df))
            elif sub_choice == 'b':
                print("Survival Rates by Class and Gender:\n", survival_rates_by_class_and_gender(df))
            elif sub_choice == 'c':
                fare_analysis_by_class(df)

        elif choice == '5':
            print("\nAdditional Insights:")
            print("a. Family Relationships and Survival")
            # Add more options as per your additional insights functions
            sub_choice = input("\nEnter your choice (a): ")
            if sub_choice == 'a':
                print("Family Relationships and Survival:\n", family_relationships_and_survival(df))

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()