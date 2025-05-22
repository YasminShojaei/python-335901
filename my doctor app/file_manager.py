import os
import pickle


def check_file(filename):
    return os.path.exists(filename)


def read_from_file(filename):
    if check_file(filename):
        if os.path.getsize(filename) > 0:
            with open(filename, "rb") as file:
                return pickle.load(file)
        else:
            return []
    else:
        with open(filename, "wb") as file:
            pass
        return []


def write_to_file(filename, data_list):
    with open(filename, "wb") as file:
        pickle.dump(data_list, file)
