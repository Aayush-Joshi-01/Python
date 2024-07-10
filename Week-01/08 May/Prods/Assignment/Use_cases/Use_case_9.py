# You are creating a program to generate usernames based on email
# addresses. Implement a Python function to extract the username from a
# given email address.

import re


def extract_username(email):
    match = re.match(r'^[^@]+', email)
    if match:
        return match.group(0)
    else:
        return ''


if __name__ == '__main__':
    username = input("Enter your email address: ")
    print(extract_username(username))
