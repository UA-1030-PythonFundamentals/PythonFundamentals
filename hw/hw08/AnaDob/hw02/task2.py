import re

def validate_password(password):
    not_met_criteria = []

    if len(password) < 6 or len(password) > 16:
        not_met_criteria.append("Minimum length 6 characters and maximum length 16 characters")

    if not re.search(r"[a-z]", password):
        not_met_criteria.append("At least one letter between [a-z]")

    if not re.search(r"[A-Z]", password):
        not_met_criteria.append("At least one letter between [A-Z]")

    if not re.search(r"\d", password):
        not_met_criteria.append("At least one number between [0-9]")

    if not re.search(r"[$#@]", password):
        not_met_criteria.append("At least one character between [$#@]")

    return not_met_criteria

def user_password():
    password = input("Enter your password: ")
    not_met_criteria = validate_password(password)

    if not_met_criteria:
        print("Invalid password. Criteria not met:")
        for criteria in not_met_criteria:
            print(f"- {criteria}")
    else:
        print("Password is valid.")

if __name__ == "__main__":
    user_password()
