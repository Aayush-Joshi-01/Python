def find_unique_exclusive_preferences(user_preference_data):
    user_exclusive_preferences = {}
    for data in user_preference_data:
        user = data["username"]
        preferences = set(data["preferences"])
        user_exclusive_preferences[user] = preferences
        for other_data in user_preference_data:
            if other_data != data:
                user_exclusive_preferences[user] -= set(other_data["preferences"])
    return user_exclusive_preferences


if __name__ == '__main__':
    user_preference_data = [
        {"username": "user1", "preferences": ["music", "movies", "books", "astronomy"]},
        {"username": "user2", "preferences": ["movies", "games", "travel"]},
        {"username": "user3", "preferences": ["books", "food", "art", "physics"]},
        {"username": "user4", "preferences": ["music", "books", "travel", "biology"]},
        {"username": "user5", "preferences": ["games", "food", "technology"]},
        {"username": "user6", "preferences": ["music", "movies", "technology"]},
    ]
    user_exclusive_preferences = find_unique_exclusive_preferences(user_preference_data)
    print(user_exclusive_preferences)
