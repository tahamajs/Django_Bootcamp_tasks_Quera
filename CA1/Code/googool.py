

import re

# pattern = r"^[a-z0-9]*\$[a-z0-9]*@gogoli\.com$"
# pattern2  = r"^.*\.go$"

def uupass_shart(Username):
    # Minimum 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character
    pattern = r"^[a-z0-9]*\$[a-z0-9]*@gogoli\.com$"
    pattern2  = r"^.*\.go$"
    return (re.match(pattern, Username) is not None ) or (re.match(pattern2, Username) is not None )


def has_only_one_dollar_sign(input_string):
    username = input_string.split('@')[0]
    pattern = r'^[^$]*\$[^$]*$'
    return bool(re.match(pattern, username))


def user_shart(input_string):
    username = input_string.split('@')[0]
    digit_count = len(re.findall(r'\d', username))
    return digit_count >= 3


# print(re.search(pattern,test_string) and count_digits_with_more_than_three_digits(test_string))

# def sharts(input_string):
#     pattern = r"\d{3,}"  # Matches sequences of 4 or more digits
#     matches = re.findall(pattern, input_string)
#     return len(matches) > 0

def pass_shart(password):
    # Minimum 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character
    pass_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&])[A-Za-z\d!@#$%^&]{8,}$"
    return re.match(pass_pattern, password) is not None




Uname = input()
Pass = input()

if pass_shart(Pass) and user_shart(Uname) and has_only_one_dollar_sign(Uname) and uupass_shart(Uname):
    print("valid")
else:
    print("invalid")