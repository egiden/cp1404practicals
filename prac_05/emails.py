"""
Emails
Estimate: 30 minutes
Actual:   ~29 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != '':
        extracted_name = extract_name_from_email(email)
        is_name_correct = input(f"Is your name {extracted_name}? (Y/n) ")
        if is_name_correct.upper() in ['Y', 'YES']:
            email_to_name[email] = extracted_name
        else:
            correct_name = input("Enter your name: ")
            email_to_name[email] = correct_name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract a name from an email address assuming that the mailbox part of the email refers to
    the name of its owner."""
    mailbox_part = email.split('@')[0]
    # If a period exists in mailbox_part, assume it serves to separate parts of the name, e.g., first nam and last name.
    if '.' in mailbox_part:
        mailbox_part = ' '.join(mailbox_part.split('.'))
    return mailbox_part.title()


main()
