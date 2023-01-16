import json

data_path = "data.json"

def read_data():
    with open(data_path) as f:
        return json.load(f)

def write_data(data, name):
    with open(name + ".json", "w") as f:
        json.dump(data, f)