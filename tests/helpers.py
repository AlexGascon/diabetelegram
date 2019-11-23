import json


def load_fixture(filename):
    file_path = f"tests/fixtures/{filename}"
    with open(file_path) as file_handler:
        return json.load(file_handler)
