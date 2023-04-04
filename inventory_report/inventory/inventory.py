from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter

report_types = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if ".csv" in path:
            data = CsvImporter.import_data(path)

        return report_types[type].generate(data)
