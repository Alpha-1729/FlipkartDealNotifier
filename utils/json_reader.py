import json


class JsonReader:
    def __init__(self, json_path):
        self.json_path = json_path

    def read_json_as_dict(self):
        with open(self.json_path, "r") as content:
            return json.load(content)
