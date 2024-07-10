def get_unique_users(post):
    users_who_liked = set(like['user'] for like in post['likes'])
    users_who_commented = set(comment['user'] for comment in post['comments'])
    return users_who_liked | users_who_commented


if __name__ == '__main__':
    post = {
        'id': 12345,
        'title': 'A great post',
        'likes': [
            {'user': 'aayush'},
            {'user': 'kaustaubh'},
            {'user': 'prankur'},
            {'user': 'aayush'}
        ],
        'comments': [
            {'user': 'aayush', 'text': 'Great post!'},
            {'user': 'aaditya', 'text': 'Thanks!'},
            {'user': 'kaustaubh', 'text': 'No problem!'}
        ]
    }
    unique_users = get_unique_users(post)
    print(unique_users)
