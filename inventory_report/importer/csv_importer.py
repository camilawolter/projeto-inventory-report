import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".csv" not in path:
            raise ValueError("Invalid File")

        with open(path, "r") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(data)
