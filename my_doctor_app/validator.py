import re


def patient_validator(patient):
    errors = []
    if not (type(patient.id) == int and patient.id > 0):
        errors.append(' ID must be an integer > 0')

    if not (type(patient.full_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", patient.full_name)):
        errors.append(' Name is Invalid')

    if not (type(patient.dr_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", patient.dr_name)):
        errors.append('Dr Name is Invalid')

    if not (type(patient.dieses) == str and re.match(r"^[a-zA-Z\s]{3,30}$", patient.dieses)):
        errors.append('Name of disease is Invalid')

    if not (type(patient.medications) == str and re.match(r"^[a-zA-Z\s]{3,30}$", patient.medications)):
        errors.append('name of medikament is Invalid')

    if not (type(patient.visit_date) == str and re.match(r"^\d{8}$", patient.visit_date)):
        errors.append('Date is Invalid')
    return errors