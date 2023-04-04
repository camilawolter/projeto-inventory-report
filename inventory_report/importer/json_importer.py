import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".json" not in path:
            raise ValueError("Invalid File")

        with open(path, "r") as file:
            data = json.load(file)
            return data
