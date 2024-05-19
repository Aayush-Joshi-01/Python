# You are developing a password strength checker program. Write a
# Python function to determine the strength of a given password based on
# the following criteria:
# 1. At least 8 characters long
# 2. Contains at least one uppercase letter, one lowercase letter, one
# digit, and one special character.

import string
import re

def password_strength(password):
    if len(password) < 8:
        return "Very weak - Less than 8 characters"
    has_upper = any(c.isupper() for c in password)
    if not has_upper:
        return "Weak - No uppercase letter"
    has_lower = any(c.islower() for c in password)
    if not has_lower:
        return "Weak - No lowercase letter"
    has_digit = any(c.isdigit() for c in password)
    if not has_digit:
        return "Weak - No digit"
    has_special = any(c in string.punctuation for c in password)
    if not has_special:
        return "Weak - No special character"

    return "Strong"

def check_password_strength(password):
    if len(password) < 8:
        return "Very weak - Less than 8 characters"
    if not re.search("[a-z]", password):
        return "Weak - No lowercase letter"
    if not re.search("[A-Z]", password):
        return "Weak - No uppercase letter"
    if not re.search("[0-9]", password):
        return "Weak - No digit"
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak - No special character"
    return "Strong"

# Example usage:
password = input("Enter your password: ")
print(password_strength(password))
password = input("Enter the password: ")
print(check_password_strength(password))