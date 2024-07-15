# Take input of age of 3 people by user and determine oldest and youngest among them.
def get_age_of_users():
    age_of_user_1 = int(input("Enter the age of user 1: "))
    age_of_user_2 = int(input("Enter the age of user 2: "))
    age_of_user_3 = int(input("Enter the age of user 3: "))
    return age_of_user_1, age_of_user_2, age_of_user_3


def youngest_and_oldest_user():
    ages = list(get_age_of_users())
    print(f"Age of youngest user is : {min(ages)}")
    print(f"Age of oldest user is : {max(ages)}")


if __name__ == '__main__':
    youngest_and_oldest_user()
