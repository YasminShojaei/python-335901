import re
from my_doctor_app.validator import patient_validator

class Patient:

    def __init__(self, id, full_name, dr_name, dieses, medications, visit_date):
        self.id = id
        self.full_name = full_name
        self.dr_name = dr_name
        self.medications = medications
        self.dieses = dieses
        self.visit_date = visit_date

    def save(self):
        print(f"{self.full_name} has been saved")

    def validate(self):
        return patient_validator(self)

    def to_tuple(self):
        return (self.id, self.full_name, self.dr_name, self.dieses, self.medications, self.visit_date)