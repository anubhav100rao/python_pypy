import json
import pandas as pd
from pprint import pprint

# Example of a nested JSON structure
nested_json = {
    "id": 1,
    "name": "John",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    },
    "projects": [
        {"name": "Project 1", "status": "Completed"},
        {"name": "Project 2", "status": "Ongoing"}
    ]
}

# Function to flatten nested JSON


def flatten_json(data, sep="_"):
    out = {}

    def helper(data, name=""):
        if type(data) is dict:
            for key, val in data.items():
                helper(val, name + key + sep)
        elif type(data) is list:
            for i, val in enumerate(data):
                helper(val, name + str(i) + sep)
        else:
            out[name[:-1]] = data

    helper(data)

    return out


# Flattening the JSON
flattened_json = flatten_json(nested_json)
pprint(flattened_json)

# Converting the flattened JSON to a DataFrame
df = pd.DataFrame([flattened_json])

print(df)
