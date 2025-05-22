import re


def person_validator(patient):
    errors = []
    if not (type(patient[0]) == int and patient[0] > 0):
        errors.append('patient ID must be an integer > 0')

    if not (type(patient[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", patient[1])):
        errors.append('patient Name is Invalid')

    if not (type(patient[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", patient[2])):
        errors.append('Dr Name is Invalid')

    if not (type(patient[3]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", patient[3])):
        errors.append('Name of disease is Invalid')

    if not (type(patient[4]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", patient[4])):
        errors.append('name of medikament is Invalid')

    if not (type(patient[5]) == str and re.match(r"^\d{8}$", patient[5])):
        errors.append('Date is Invalid')
    return errors
