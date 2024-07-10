def find_unique_users_with_permissions(user_data, read_permission, write_permission):
    unique_users = set()
    for data in user_data:
        if read_permission in data["permissions"] and write_permission in data["permissions"]:
            unique_users.add(data["username"])
    return unique_users


if __name__ == '__main__':
    user_data = [
        {"username": "user1", "permissions": ["read", "write"]},
        {"username": "user2", "permissions": ["read"]},
        {"username": "user3", "permissions": ["write"]},
        {"username": "user4", "permissions": ["read", "write"]},
        {"username": "user5", "permissions": ["read"]},
        {"username": "user6", "permissions": ["write"]},
        {"username": "user7", "permissions": ["read", "write"]},
        {"username": "user8", "permissions": ["read"]},
        {"username": "user9", "permissions": ["write"]},
    ]
    unique_users = find_unique_users_with_permissions(user_data, "read", "write")
    print(unique_users)
