def get_unique_preferences(user_preferences):
    return set().union(*user_preferences.values())


if __name__ == '__main__':
    user_preferences = {
        "user1": ["preference1", "preference2", "preference3"],
        "user2": ["preference2", "preference3", "preference4"],
        "user3": ["preference1", "preference4", "preference5"],
    }
    unique_preferences = get_unique_preferences(user_preferences)
    print(unique_preferences)
