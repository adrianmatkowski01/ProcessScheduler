import json

def read_data(data_path):
    with open(data_path) as f:
        return json.load(f)

def write_data(data, name):
    with open(name + ".json", "w") as f:
        json.dump(data, f, indent=4)