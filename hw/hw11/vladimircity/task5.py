import re

def check(login):
    pattern = r"^(admin|employee)(-|id|-id)(\d+)$"
    match = re.match(pattern, login.lower())
    if match:
        return True
    else:
        raise ValueError(f"incorrect login '{login}'")


test_strings = [
    "ADMIN-ID124",
    "admin-iD3457",
    "AdMinid2",
    "ADmin-569",
    "employee-124",
    "emPloyee-124",
    "EMPLOYEE-4689",
    "__EMPLOYEE-4689"
]

for string in test_strings:
    try:
        if check(string):
            print("checked successfully")
    except ValueError as e:
        print(f"checked not successfully with {string}")
