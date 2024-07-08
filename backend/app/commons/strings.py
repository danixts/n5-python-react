import re


def is_valid_email(email):
    # Define the regex pattern for a valid email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use the re.match function to check if the email matches the pattern
    if re.match(email_regex, email):
        return True
    else:
        return False
