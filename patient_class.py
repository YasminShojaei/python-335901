import re


class Patient:

    def __init__(self, id, full_name, dr_name, dieses, medications, date):
        self.id = id
        self.full_name = full_name
        self.dr_name = dr_name
        self.medications = medications
        self.dieses = dieses
        self.date = date

    def save(self):
        print(f"{self.full_name} has been saved")

    def person_validator(self):
        errors = []
        if not (type(self.id) == int and self.id > 0):
            errors.append(' ID must be an integer > 0')

        if not (type(self.full_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", self.full_name)):
            errors.append(' Name is Invalid')

        if not (type(self.dr_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", self.dr_name)):
            errors.append('Dr Name is Invalid')

        if not (type(self.dieses) == str and re.match(r"^[a-zA-Z\s]{3,30}$", self.dieses)):
            errors.append('Name of disease is Invalid')

        if not (type(self.medications) == str and re.match(r"^[a-zA-Z\s]{3,30}$", self.medications)):
            errors.append('name of medikament is Invalid')

        if not (type(self.date) == str and re.match(r"^\d{8}$", self.date)):
            errors.append('Date is Invalid')
        return errors
