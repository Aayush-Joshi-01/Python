# . You are building a program to analyse text data. Implement a Python function to extract all email addresses from a given text string.
import re
def extract_emails(email):
    # this is a fucntion to extract all email addresses from the given string
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # this a regex to identify email addresses by checking all the permutations of valid characters ina an email address
    emails = re.findall(pattern, email)
    return emails
text = "Please contact us at aayushjoshi.dev@gmail.com or joshi.aayush@yash.com or merlin%jennifer@neobrite.uk. Thank you."
emails = extract_emails(text)
print(emails)