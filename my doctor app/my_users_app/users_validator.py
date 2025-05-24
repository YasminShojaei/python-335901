import re


def user_validator(user):
    error = []
    if not (type(user[0]) == int and user[0] > 0):
        error.append("User ID must be > 0!")

    if not (type(user[1]) == str and re.match(r"^[a-zA-z\s]{3,30}$", user[1])):
        error.append("Name/Famly is INVALID!")

    if not (type(user[2]) == str and re.match(r"^[@a-zA-z]{5,15}$", user[2])):
        error.append("Username is INVALID!")

    if not (type(user[3] == str and re.match(r"^[a-zA-z]{5,10}\d{1,3}$", user[3]))):
        error.append("Password is INVALID!")

    if not isinstance(user[4], str):
        error.append("Status must be True or False!")

    return error
