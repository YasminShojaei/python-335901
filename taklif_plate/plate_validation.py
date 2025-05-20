import re


def plate_validation(plate):
    pattern = r"\d{2}[آ-ی]{1}\d{3,5}"
    return re.match(pattern, plate)
