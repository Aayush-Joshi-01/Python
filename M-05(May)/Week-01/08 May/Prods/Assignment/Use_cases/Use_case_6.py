# You are developing a program to format phone numbers. Write a
# Python function to format a given string as a phone number in the
# format (XXX) XXX-XXXX.
def format_phone_number(string):
    # Remove all non-numeric characters from the string
    numeric_filter = filter(str.isdigit, string)
    numeric_string = "".join(numeric_filter)

    # Format the string as a phone number (XXX) XXX-XXXX
    return f"({numeric_string[:3]}) {numeric_string[3:6]}-{numeric_string[6:10]}"


# Example usage
phone_number = input("Enter a phone number: ")
formatted_phone_number = format_phone_number(phone_number)
print(f"Formatted phone number: {formatted_phone_number}")
