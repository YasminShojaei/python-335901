import os
import pickle


def check_file(file_name):
    return os.path.exists(file_name)


def read_from_file(file_name):
    if check_file(file_name):
        if os.path.getsize(file_name) > 0:
            with open(file_name, "rb") as file:
                return pickle.load(file)
        else:
            return []
    else:
        with open(file_name, "wb") as file:
            pass
    return []


def write_to_file(file_name, data_list):
    with open(file_name, "wb") as file:
        pickle.dump(data_list, file)
